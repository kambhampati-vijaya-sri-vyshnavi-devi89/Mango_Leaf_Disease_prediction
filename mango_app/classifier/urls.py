from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_view, name='predict'),
    path('history/', views.history_view, name='history'),
    path('scan/<int:scan_id>/', views.scan_detail, name='scan_detail'),
    path('scan/<int:scan_id>/feedback/', views.submit_feedback, name='submit_feedback'),
    path('scan/<int:scan_id>/report/', views.download_report, name='download_report'),
    path('scan/<int:scan_id>/delete/', views.delete_scan, name='delete_scan'),
    path('api/stats/', views.stats_api, name='stats_api'),
]
