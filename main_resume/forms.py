from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Your First and Last name', max_length = 100)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length=2000)

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = "From: {0}\n{1}".format(
        self.cleaned_data["name"],
        self.cleaned_data["message"],
        self.cleaned_data["email_address"]
        )
        send_mail(
        "Site message",
        message,
        "patrickidungafa2@gmail.com",
        ["patrickidungafa2@gmail.com"],
        fail_silently=False,
        )