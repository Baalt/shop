from django.contrib import admin

from .models import Glasses


class GlassesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'image')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Glasses, GlassesAdmin)
