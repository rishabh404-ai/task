from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    list_filter = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    search_fields = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)

admin.site.register(Register,RegisterAdmin)    