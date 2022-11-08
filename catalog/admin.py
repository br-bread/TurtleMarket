from django.contrib import admin

from catalog.models import Category, Gallery, Item, Tag

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb',)
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


@admin.register(Gallery)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item')
