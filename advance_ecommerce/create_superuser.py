from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

def create_superuser():
    User = get_user_model()
    email = "admin@example.com"
    password = "admin123"
    first_name = "Admin"
    last_name = "User"
    username = "admin"

    try:
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_superuser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            print("✅ Superuser created successfully:", email)
        else:
            print("ℹ️ Superuser already exists:", email)
    except IntegrityError:
        print("⚠️ Superuser already created.")
