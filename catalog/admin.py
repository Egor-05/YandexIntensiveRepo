from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import CatalogCategory, CatalogItem, CatalogTag, Photo, Photos

# Register your models here.


class PhotosAdmin(admin.StackedInline):
    model = Photos


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image_tmb",
    )


@admin.register(CatalogItem)
class ItemAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "is_published",
        "image_tmb",
    )
    filter_horizontal = ("tags",)
    inlines = [PhotosAdmin]
    summernote_fields = ("text",)

    def get_list_editable(self, request):
        """
        get_list_editable method implementation,
        django ModelAdmin doesn't provide it.
        """
        dynamically_editable_fields = ("is_published",)
        return dynamically_editable_fields

    def get_changelist_instance(self, request):
        """
        override admin method and list_editable property value
        with values returned by our custom method implementation.
        """
        self.list_editable = self.get_list_editable(request)
        return super(ItemAdmin, self).get_changelist_instance(request)


@admin.register(CatalogTag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )


@admin.register(CatalogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
        "weight",
    )
