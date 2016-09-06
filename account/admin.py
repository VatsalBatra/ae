from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','is_active','is_superuser','username']
    search_fields = ['first_name', 'username', 'email']
    actions_on_bottom = True
#date_hierarchy = 'date_joined' why this is showing error
# Register your models here.
