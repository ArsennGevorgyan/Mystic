from django.db import models

from helpers.media_upload import upload_menu_item_images, upload_bar_item_images


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BarCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='bar_category_items')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_menu_item_images, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='menu_items')

    def __str__(self):
        return self.name


class BarItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_bar_item_images, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(BarCategory, on_delete=models.CASCADE,
                                 related_name='bar_items')

    def __str__(self):
        return self.name


class Hookah(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return self.name
