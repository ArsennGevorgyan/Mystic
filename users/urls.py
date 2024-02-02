from django.urls import path
from .views import EmailView, LoginView, RegistrationView, ValidateUserLink, LogoutView, UserUpdate, \
    UserProfile

app_name = "users"

urlpatterns = [
    path("send-email/", EmailView.as_view(), name="send_email"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("<int:pk>/<str:token>/", ValidateUserLink.as_view(), name="verify"),
    path('update-user/<int:pk>/', UserUpdate.as_view(), name='update_user'),
    path('users/detail/<int:pk>/', UserProfile.as_view(), name='user_profile'),
]
