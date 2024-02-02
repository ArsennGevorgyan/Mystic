from django.urls import path
from menu.views import MenuItemView, BarItemView, HookahListView, BarItemDetailView

app_name = 'menu'

urlpatterns = [
    path("", MenuItemView.as_view(), name="menu_items"),
    path("bar-items/", BarItemView.as_view(), name="bar_items"),
    path("hookahs/", HookahListView.as_view(), name="hookahs"),
    path('bar-items/<int:pk>/', BarItemDetailView.as_view(), name='bar_item_detail'),
]
