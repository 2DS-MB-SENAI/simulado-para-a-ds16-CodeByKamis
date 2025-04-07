from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UserinhoAdmin(UserAdmin):
    list_display = ('telefone',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone',)}),
    )

admin.site.register(Usuario, UserinhoAdmin)
# Register your models here.
