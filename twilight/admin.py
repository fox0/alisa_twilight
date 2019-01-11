from django.contrib import admin
from twilight.models import Log, TTSSpr


class LogAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'ask', 'ans')
    list_filter = ('user_id',)


admin.site.register(Log, LogAdmin)


class TTSSprAdmin(admin.ModelAdmin):
    list_display = ('word', 'speech')


admin.site.register(TTSSpr, TTSSprAdmin)
