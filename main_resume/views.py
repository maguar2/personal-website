from django.shortcuts import render
from . import forms
from django.views.generic.edit import FormView



def home(request):
    return render(request, 'main_resume/home.html')

def success(request):
    return render(request, 'main_resume/success.html')

class ContactView(FormView):
    template_name = "main_resume/contact.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


