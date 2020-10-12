from django.contrib import admin
from .models import Register, Entry

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    list_filter = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)
    search_fields = ('name','idcard_no','id_type','address','phone_no','email','meet_with',)

admin.site.register(Register,RegisterAdmin)    


class EntryAdmin(admin.ModelAdmin):
    list_display = ('person','start_time','end_time',)
    list_filter = ('person','start_time','end_time',)
    search_fields = ('person','start_time','end_time',)

admin.site.register(Entry,EntryAdmin)