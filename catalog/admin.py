from django.contrib import admin

from catalog.models import Category, GalleryImage, Item, MainImage, Tag

admin.site.register(Category)
admin.site.register(Tag)


class MainImageInline(admin.TabularInline):
    model = MainImage
    extra = 0
    readonly_fields = ('image_tmb',)
    fields = ('upload', 'image_tmb',)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        MainImageInline,
        GalleryImageInline,
    ]
    list_display = ('image_tmb', 'name', 'category', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


@admin.register(MainImage)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tmb', 'upload',)
    list_editable = ('upload',)
    list_display_links = ('image_tmb',)


@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'image_tmb', 'upload',)
    list_editable = ('upload',)
    list_display_links = ('image_tmb',)
