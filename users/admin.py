from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseAdmin):
    inlines = (ProfileAdmin, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)