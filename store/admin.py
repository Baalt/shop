from django.contrib import admin

from .models import Glasses, CustomerReviews


class GlassesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'image')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class RevievAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'review', 'image')
    list_display_links = ('client_name', 'review', 'image')
    search_fields = ('client_name', 'review')


admin.site.register(Glasses, GlassesAdmin)
admin.site.register(CustomerReviews, RevievAdmin)
