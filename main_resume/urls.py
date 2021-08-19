from django.urls import path
from . import views

app_name = 'main_resume'

urlpatterns = [
    path('', views.home, name='home'),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("success/", views.success, name="success"),
]
