import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advance_ecommerce.settings')

application = get_wsgi_application()

# Auto-create superuser
try:
    from advance_ecommerce.create_superuser import create_superuser
    create_superuser()
except Exception as e:
    print("⚠️ Auto-create superuser failed:", e)
