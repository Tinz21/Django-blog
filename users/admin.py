from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from users.models import User


@admin.register(User)
class UserAdmin(BaseUser):
    pass
