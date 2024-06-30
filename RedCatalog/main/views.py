
from django.shortcuts import render, redirect
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse



def index(request):

    return render(request, 'main/index.html', {"city": 'Moscow'})

def registration(request):
    return render(request, 'main/registration.html', {"city": 'Москва'})

def sign_up(request):
    data = request.POST.get
    mail = data("mail")
    password = data("password")
    password_confirm = data("password-confirm")
    firstname = data("firstname")
    lastname = data("lastname")
    birthdate = data("birthdata")
    photo = data("photo")

    user = User.objects.create_user(username=mail, password=password)
    user.first_name = firstname
    user.last_name = lastname
    user.save()
    auth.login(request, user)
    return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')

class LoginView(View):
    def get(self, request):
        mail = request.GET.get('mail')
        password = request.GET.get('password')
        if len(password) == 0 or len(mail) == 0:
            return JsonResponse({'error': 2}, status=200)
        if len(mail.split('@')) != 2:
            return JsonResponse({'error': 3}, status=200)
        user = auth.authenticate(request, username=mail, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'error': 0}, status=200)

        return JsonResponse({'error': 1}, status=200)
