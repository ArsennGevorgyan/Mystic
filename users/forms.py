from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    country = CountryField().formfield()
    phone_number = PhoneNumberField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "country", "email",
                  "phone_number", "image")
