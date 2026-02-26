import numpy as np
from PIL import Image
import io
import os

_model = None

DEFAULT_CLASS_NAMES = [
    'Anthracnose',
    'Bacterial Canker',
    'Cutting Weevil',
    'Die Back',
    'Gall Midge',
    'Healthy',
    'Powdery Mildew',
    'Sooty Mould',
]


def get_model():
    global _model
    if _model is None:
        from django.conf import settings
        import tensorflow as tf
        model_path = str(settings.MODEL_PATH)
        if os.path.exists(model_path):
            _model = tf.keras.models.load_model(model_path)
        else:
            raise FileNotFoundError(
                f"Model not found at {model_path}. "
                "Please place 'mango_leaf_model.keras' in the project root (same folder as manage.py)."
            )
    return _model


def preprocess_image(image_bytes, img_size=224):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((img_size, img_size))
    arr = np.array(img, dtype=np.float32)
    arr = (arr / 127.5) - 1.0  # MobileNetV2 normalization
    return np.expand_dims(arr, axis=0)


def predict(image_bytes):
    model = get_model()
    arr = preprocess_image(image_bytes)
    preds = model.predict(arr, verbose=0)[0]
    results = [
        {'label': DEFAULT_CLASS_NAMES[i], 'confidence': float(preds[i]) * 100}
        for i in range(len(DEFAULT_CLASS_NAMES))
    ]
    results.sort(key=lambda x: x['confidence'], reverse=True)
    return results
