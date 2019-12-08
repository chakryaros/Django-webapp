from django.contrib import admin

# Register your models here.
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email')
    list_filter = ('email',)

admin.site.register(UserProfile, UserProfileAdmin)