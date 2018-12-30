from django.shortcuts import render
from base.models import SubscriptionType, Settings, Message
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def subscription(request):
    try:
        setting = Settings.objects.first()
        txt = setting.roles
    except:
        txt =''
    return render(request, 'subscription.html', {'type': SubscriptionType.objects.filter(active=True),
                                                 'txt':txt})


def Newslogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return redirect(settings.LOGOUT_REDIRECT_URL)

def Newslogout(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def NewsRegister(request):

    if request.method == 'POST':
        newpwd = request.POST.get('newpwd')
        newemail = request.POST.get('newemail')
        name = request.POST.get('name')

        if User.objects.filter(Q(email=newemail)|Q(username=name)).exists():
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            user = User.objects.create(username=name, email=newemail)
            user.set_password(newpwd)
            user.save()
            return redirect(settings.LOGIN_REDIRECT_URL)

def ContactUs(request):
    try:
        settings_obj = Settings.objects.first()
        contact_us = {'email':settings_obj.email,
                      'tel':settings_obj.telehphone,
                      'postalcode': settings_obj.postalcode,
                      'address':settings_obj.address,
                      'message':settings_obj.message}
    except:
        contact_us = {'email':'',
                      'tel':'',
                      'postalcode': '',
                      'address':'',
                      'message':''}
    return render(request, 'contact_us.html', {'contact_us':contact_us})


def ContactUsMessage(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        name = request.POST.get('name',None)
        message = request.POST.get('message',None)

        if None not in [email, name, message]:
            Message.objects.create(email=email,
                                   name=name,
                                   message=message)
        return render(request)
    else:
        return render(request)