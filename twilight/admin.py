from django.contrib import admin
from twilight.models import TTSSpr


class TTSSprAdmin(admin.ModelAdmin):
    list_display = ('word', 'speech')


admin.site.register(TTSSpr, TTSSprAdmin)
