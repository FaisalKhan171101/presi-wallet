from django.shortcuts import render


def index(request):
    return render(request, 'wallet/home_1.html')
