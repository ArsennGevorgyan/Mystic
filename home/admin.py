from django.contrib import admin
from django.utils.html import format_html

from .models import AboutUs, Chef, WhyChooseUs, ContactUs, FollowUs, Gallery, Events

from django.templatetags.static import static


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "thumbnail")
    list_display_links = ("title",)
    search_fields = ("title",)
    readonly_fields = ("thumbnail",)
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("title",)},
        ),
        (
            "INFO",
            {
                "fields": (
                    "content",
                    ("image", "thumbnail"),
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


class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "thumbnail")
    list_display_links = ("title",)
    search_fields = ("title",)
    readonly_fields = ("thumbnail",)
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("title",)},
        ),
        (
            "INFO",
            {
                "fields": (
                    "content",
                    ("image", "thumbnail"),
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


class ChefAdmin(admin.ModelAdmin):
    list_display = ("name", "bio", "thumbnail")
    list_display_links = ("name",)
    search_fields = ("name",)
    readonly_fields = ("thumbnail",)
    fieldsets = (
        (
            "GENERAL",
            {"fields": ("name",)},
        ),
        (
            "INFO",
            {
                "fields": (
                    "bio",
                    ("image", "thumbnail"),
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


class FollowUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'email', 'opening_hours')


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(FollowUs, FollowUsAdmin)
admin.site.register(Gallery)
admin.site.register(Events)
