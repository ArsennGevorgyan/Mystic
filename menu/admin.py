from django.contrib import admin
from django.utils.html import format_html
from menu.models import MenuItem, BarItem, Category, BarCategory, Hookah
from django.templatetags.static import static


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at", "thumbnail")
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name", "price",)},
        ),
        (
            "INFO",
            {
                "fields": (
                    "category",
                    "description",
                    ("image", "thumbnail"),
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    @staticmethod
    def thumbnail(obj):
        return format_html(
            "<img src='{}' class='thumbnail'>",
            obj.image.url if obj.image else static("img/no_image.jpg"),
        )


class BarItemAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at", "thumbnail")
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name", "price",)},
        ),
        (
            "INFO",
            {
                "fields": (
                    "category",
                    "description",
                    ("image", "thumbnail"),
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    @staticmethod
    def thumbnail(obj):
        return format_html(
            "<img src='{}' class='thumbnail'>",
            obj.image.url if obj.image else static("img/no_image.jpg"),
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class BarCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class HookahAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(BarItem, BarItemAdmin)
admin.site.register(Hookah, HookahAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BarCategory, BarCategoryAdmin)
