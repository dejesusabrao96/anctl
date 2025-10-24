from django.contrib import admin
from .models import TipuRelatoriu, Relatoriu

@admin.register(TipuRelatoriu)
class TipuRelatoriuAdmin(admin.ModelAdmin):
    list_display = ['naran', 'deskrisaun']

@admin.register(Relatoriu)
class RelatoriuAdmin(admin.ModelAdmin):
    list_display = ['titulu', 'tipu_relatoriu', 'data']
    list_filter = [ 'tipu_relatoriu', 'data']
    search_fields = ['titulu']