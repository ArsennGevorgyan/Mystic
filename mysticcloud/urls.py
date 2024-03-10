from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('users.urls', namespace='users')),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    path("change-password/", auth_views.PasswordChangeView.as_view()),
    path("reset-password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
