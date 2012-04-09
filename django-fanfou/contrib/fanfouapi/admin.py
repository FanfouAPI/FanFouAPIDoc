from fanfouapi.models import FFUser
from django.contrib import admin


class FFUserAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('loginname', 'screen_name', 'login_time',)
    search_fields = ('screen_name', 'loginname',)


admin.site.register(FFUser, FFUserAdmin)
