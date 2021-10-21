from django.contrib import admin

from .models import User

class UserList(admin.ModelAdmin):
    list_display = ['membership_status', 'name' , 'status' , 'category_type', 'user_type' , 'department_type' , 'address', 'remarks',  'update' , 'image']
    list_filter = ['status', 'category_type', 'user_type' , 'department_type']

admin.site.register(User, UserList)