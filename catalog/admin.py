from django.contrib import admin

from catalog.models import Category, Gallery, Item, Preview, Tag

admin.site.register(Category)
admin.site.register(Tag)


class PreviewImage(admin.TabularInline):
    model = Preview
    extra = 0
    readonly_fields = ('image_tmb',)
    fields = ('upload', 'image_tmb',)


class GalleryImage(admin.TabularInline):
    model = Gallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        PreviewImage,
        GalleryImage,
    ]
    list_display = ('name', 'category', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tmb', 'upload',)
    list_editable = ('upload',)
    list_display_links = ('image_tmb',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tmb', 'upload',)
    list_editable = ('upload',)
    list_display_links = ('image_tmb',)
