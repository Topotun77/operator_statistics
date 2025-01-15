from django.contrib import admin

from .models import Base, Call

# admin.site.register(Call)
admin.site.register(Base)


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'operator', 'success', 'duration', 'base')
    fieldsets = (
        ('Description', {
            'fields': ('campaign',
                       'operator',
                       'base')
        }),
        ('Parameters', {
            'fields': (('number', ),
                       ('start_time', 'end_time', 'duration'),
                       ('processed', 'status', 'success'),
                       )
        })
    )
    search_fields = ('campaign', 'operator', 'base')
    list_filter = ('campaign', 'operator', 'base', 'success')
