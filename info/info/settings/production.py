from .base import *

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
    )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')