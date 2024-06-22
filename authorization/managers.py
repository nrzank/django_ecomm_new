from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        if not username:
            raise ValueError('ValueError')
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self.create_user(username, password, is_staff=True, is_active=True)



