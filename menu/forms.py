from django import forms
from .models import MenuItem, BarItem, Category


class MenuItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop("owner") if kwargs.get("owner") else None
        super().__init__(*args, **kwargs)
        if owner:
            self.fields["category"].queryset = Category.objects.filter(owner=owner)

    class Meta:
        model = MenuItem
        fields = ("name", "price", "description",
                  "image", "restaurant")


class BarItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop("owner") if kwargs.get("owner") else None
        super().__init__(*args, **kwargs)
        if owner:
            self.fields["category"].queryset = Category.objects.filter(owner=owner)

    class Meta:
        model = BarItem
        fields = ("name", "price", "description",
                  "image", "restaurant")


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["creation_date"].widget.attrs.update(
            {"class": "form-control"})

    class Meta:
        model = Category
        fields = ("name",)
