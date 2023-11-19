from django.shortcuts import render, HttpResponse


# Create your views here.
def DjangoHome(request):
    return render(request, 'home.html')


def Accounts(request):
    return render(request, 'login.html')
