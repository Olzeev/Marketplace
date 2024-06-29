
from django.shortcuts import render, redirect
import django.contrib.auth as auth
from django.views.generic import View
from django.http import JsonResponse

def index(request):
    print(request)
    return render(request, 'main/index.html', {"city": 'Москва'})

def registration(request):
    mail = request.POST.get('mail')
    password = request.POST.get('password')
    user = auth.authenticate(email=mail, password=password)
    if user is not None:

        return render(request, 'main/registration.html', {"city": 'Москва'})


class LoginView(View):
    def get(self, request):
        mail = request.GET.get('mail')
        password = request.GET.get('password')

        user = auth.authenticate(request, username=mail, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'error': 0}, status=200)

        return JsonResponse({'error': 1}, status=200)