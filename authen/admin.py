from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authen.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ( 'name','facilityid','username','idnumber','position','phone','facadmin','itemadmin','reportadmin','useradmin','created_at','updated_at')
    list_filter = ( 'name','facilityid','username','idnumber','position','phone','facadmin','itemadmin','reportadmin','useradmin','created_at','updated_at')
    fieldsets = (
        ('infos', {'fields': ('name','facilityid','username','idnumber','position','phone','facadmin','itemadmin','reportadmin','useradmin','created_at','updated_at')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    
    search_fields = ('name','facilityid','username','idnumber','position','phone','facadmin','itemadmin','reportadmin','useradmin','created_at','updated_at')
    ordering = ('name','facilityid','username','idnumber','position','phone','facadmin','itemadmin','reportadmin','useradmin','created_at','updated_at')
      
