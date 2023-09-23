from django.contrib import admin
from .models import *
# Register your models here.
class SorovAdmin(admin.ModelAdmin):
    model = Sorov
    list_display = ['fish','idpassport','Yashashmanzili','mfynomi','kochanomi','telefonraqami',]
admin.site.register(Sorov,SorovAdmin)

admin.site.register(Hokimiyat)
admin.site.register(Orinbosar)
admin.site.register(Tashkilotlar)