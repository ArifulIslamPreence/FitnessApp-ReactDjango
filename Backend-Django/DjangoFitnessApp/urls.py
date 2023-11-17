from . import views
from django.urls import path

urlpatterns = [
    path("", views.DjangoHome, name = 'DjangoHome'),
    path("", views.Accounts, name = 'Accounts')
]