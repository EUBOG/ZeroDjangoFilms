import os

# Внизу файла, после STATIC_URL:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')