from django.contrib import admin
from .models import CatalogTag, CatalogItem, CatalogCategory

# Register your models here.


@admin.register(CatalogItem)
class Item(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )

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
        return super(Item, self).get_changelist_instance(request)


@admin.register(CatalogTag)
class Tag(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
    )


@admin.register(CatalogCategory)
class Category(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
        "weight",
    )
