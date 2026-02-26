from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
import base64
import json
import uuid
import os

from .models import ScanHistory, Feedback
from .disease_data import get_disease_info


def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


# ─── MAIN PAGE ───────────────────────────────────────────────────────────────

def index(request):
    # Stats for dashboard
    total_scans = ScanHistory.objects.count()
    disease_counts = {}
    for scan in ScanHistory.objects.values('top_disease'):
        d = scan['top_disease']
        disease_counts[d] = disease_counts.get(d, 0) + 1
    top_diseases = sorted(disease_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    return render(request, 'classifier/index.html', {
        'total_scans': total_scans,
        'top_diseases': top_diseases,
    })


# ─── PREDICT ─────────────────────────────────────────────────────────────────

@csrf_exempt
@require_http_methods(["POST"])
def predict_view(request):
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image file provided.'}, status=400)

    image_file = request.FILES['image']
    allowed_types = ['image/jpeg', 'image/png', 'image/webp', 'image/jpg']
    if image_file.content_type not in allowed_types:
        return JsonResponse({'error': 'Invalid file type. Use JPEG, PNG, or WEBP.'}, status=400)
    if image_file.size > 10 * 1024 * 1024:
        return JsonResponse({'error': 'File too large. Max 10MB.'}, status=400)

    image_bytes = image_file.read()
    b64 = base64.b64encode(image_bytes).decode('utf-8')
    mime = image_file.content_type

    try:
        from .ml import predict
        results = predict(image_bytes)
    except FileNotFoundError as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'Prediction failed: {str(e)}'}, status=500)

    top = results[0]
    is_healthy = top['label'].lower() == 'healthy'
    disease_info = get_disease_info(top['label'])

    # Save to database
    scan = ScanHistory(
        session_key=_get_session_key(request),
        top_disease=top['label'],
        top_confidence=top['confidence'],
        all_predictions=results,
        is_healthy=is_healthy,
    )
    ext = image_file.name.split('.')[-1] if '.' in image_file.name else 'jpg'
    scan.image.save(f"{uuid.uuid4().hex}.{ext}", ContentFile(image_bytes), save=False)
    scan.save()

    return JsonResponse({
        'success': True,
        'scan_id': scan.id,
        'predictions': results,
        'image_data': f'data:{mime};base64,{b64}',
        'top': top,
        'is_healthy': is_healthy,
        'disease_info': {
            'scientific_name': disease_info['scientific_name'],
            'type': disease_info['type'],
            'severity': disease_info['severity'],
            'severity_color': disease_info['severity_color'],
            'description': disease_info['description'],
            'symptoms': disease_info['symptoms'],
            'treatment': disease_info['treatment'],
            'prevention': disease_info['prevention'],
            'spread_control': disease_info['spread_control'],
            'organic_options': disease_info.get('organic_options', []),
        },
    })


# ─── HISTORY ─────────────────────────────────────────────────────────────────

def history_view(request):
    scans = ScanHistory.objects.all()
    # Filter
    search = request.GET.get('search', '').strip()
    disease_filter = request.GET.get('disease', '').strip()
    if search:
        scans = scans.filter(top_disease__icontains=search)
    if disease_filter:
        scans = scans.filter(top_disease=disease_filter)

    paginator = Paginator(scans, 12)
    page = paginator.get_page(request.GET.get('page', 1))

    all_diseases = ScanHistory.objects.values_list('top_disease', flat=True).distinct()

    return render(request, 'classifier/history.html', {
        'page': page,
        'search': search,
        'disease_filter': disease_filter,
        'all_diseases': sorted(all_diseases),
        'total': scans.count(),
    })


def scan_detail(request, scan_id):
    scan = get_object_or_404(ScanHistory, id=scan_id)
    disease_info = get_disease_info(scan.top_disease)
    has_feedback = hasattr(scan, 'feedback')
    return render(request, 'classifier/detail.html', {
        'scan': scan,
        'disease_info': disease_info,
        'has_feedback': has_feedback,
    })


# ─── FEEDBACK ────────────────────────────────────────────────────────────────

@csrf_exempt
@require_http_methods(["POST"])
def submit_feedback(request, scan_id):
    scan = get_object_or_404(ScanHistory, id=scan_id)

    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    rating = int(data.get('rating', 0))
    if not (1 <= rating <= 5):
        return JsonResponse({'error': 'Rating must be 1–5'}, status=400)

    correct_diag_raw = data.get('correct_diagnosis')
    if correct_diag_raw == 'true':
        correct_diagnosis = True
    elif correct_diag_raw == 'false':
        correct_diagnosis = False
    else:
        correct_diagnosis = None

    Feedback.objects.update_or_create(
        scan=scan,
        defaults={
            'rating': rating,
            'correct_diagnosis': correct_diagnosis,
            'correct_disease': data.get('correct_disease', ''),
            'comment': data.get('comment', ''),
        }
    )
    return JsonResponse({'success': True})


# ─── REPORT DOWNLOAD ─────────────────────────────────────────────────────────

def download_report(request, scan_id):
    scan = get_object_or_404(ScanHistory, id=scan_id)
    disease_info = get_disease_info(scan.top_disease)
    try:
        from .report import generate_report
        docx_bytes = generate_report(scan, disease_info)
        filename = f"MangoScan_Report_{scan.id:06d}_{scan.top_disease.replace(' ', '_')}.docx"
        response = HttpResponse(
            docx_bytes,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    except ImportError:
        return HttpResponse("python-docx not installed. Run: pip install python-docx", status=500)
    except Exception as e:
        return HttpResponse(f"Report generation failed: {str(e)}", status=500)


# ─── DELETE SCAN ─────────────────────────────────────────────────────────────

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_scan(request, scan_id):
    scan = get_object_or_404(ScanHistory, id=scan_id)
    # Delete image file
    if scan.image:
        try:
            os.remove(scan.image.path)
        except Exception:
            pass
    scan.delete()
    return JsonResponse({'success': True})


# ─── STATS API ───────────────────────────────────────────────────────────────

def stats_api(request):
    from django.db.models import Count, Avg
    disease_counts = (
        ScanHistory.objects.values('top_disease')
        .annotate(count=Count('id'), avg_conf=Avg('top_confidence'))
        .order_by('-count')
    )
    total = ScanHistory.objects.count()
    healthy_count = ScanHistory.objects.filter(is_healthy=True).count()

    return JsonResponse({
        'total_scans': total,
        'healthy_count': healthy_count,
        'disease_count': total - healthy_count,
        'disease_breakdown': list(disease_counts),
    })
