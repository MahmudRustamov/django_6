from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from anymail.exceptions import AnymailAPIError
from .tokens import account_activation_token

def send_email_confirmation(user, request):
    token = account_activation_token.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    confirmation_link = request.build_absolute_uri(
        reverse('accounts:confirmation', kwargs={'uidb64': uidb64, 'token': token})
    )

    subject = "Confirm Your Email Address"
    html_message = render_to_string('auth/email_confirmation.html', {
        'user': user,
        'confirmation_link': confirmation_link,
    })

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.content_subtype = 'html'

    try:
        email.send()
    except AnymailAPIError as e:
        print("Error while sending the email:", e)
