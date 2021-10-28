import os
from contextvars import Token

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse

from rest_framework.request import Request


class EmailUtils:
    @staticmethod
    def _send_email(to: str, template_name: str, contex: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(contex)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register_email(cls, address: str, name: str, token: Token, request: Request) -> None:
        uri = request.build_absolute_uri(reverse('auth_activate', args=(token)))
        cls._send_email(address, 'register.html', {'name': name, 'url': uri}, 'Register')
