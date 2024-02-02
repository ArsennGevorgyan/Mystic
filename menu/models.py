from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)

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
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) if self.name else slugify(self.category)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Hookah(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return self.name
