
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from users.generate_token import account_activation_token

User = get_user_model()


@shared_task
def send_simple_email(body, subject, email):
    print(email)
    send_mail(subject, body, from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email])


@shared_task
def registration_mail(subject, user_id, current_site):
    user = User.objects.get(pk=user_id)
    token = account_activation_token.make_token(user)
    message = render_to_string("users/authentication.html",
                               {"users": user,
                                "domain": current_site,
                                "token": token,
                                "user_pk": user.pk})
    email = EmailMessage(subject=subject, body=message,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[user.email])
    email.send(fail_silently=False)
