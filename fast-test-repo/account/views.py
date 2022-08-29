from django.shortcuts import render
import random
from django.contrib import messages
from .models import Profile,MyUser
from django.http import HttpResponse , Http404
from kavenegar import *
import uuid
from django.contrib.auth.hashers import make_password

# Create your views here.

def send_sms_test(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        phone = request.POST.get('phone')
        if MyUser.objects.filter(phone=phone):
            MyUser.objects.filter(phone=phone).update(token=number)
        else:
            MyUser.objects.create(username=phone,phone=phone,token=number)
            
    api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
    params = { 'sender' : '10000080808880', 'receptor': f'{phone}', 'message' :f'{number}' }
    api.sms_send( params)
    response = render(request,'verify.html')
    x = phone
    response.set_cookie('phone_number_cookie',x,1000)
    return response

def VerifyChecked(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        try :
            user = MyUser.objects.get(phone= phone_c)
        except:
            return HttpResponse('error')
        if user.token == token :
            return render(request,'complateprofile.html')
        else :
            return HttpResponse('error 2')


def ComplateProfileView(request):
    return render(request,'complateprofile.html',{})

def ComplateProfile(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        phone_c = request.COOKIES['phone_number_cookie']
        MyUser.objects.filter(phone=phone_c).update(
            username=username,password=make_password(password)
        )
        return HttpResponse("Done")

def respass(request):
    return render(request,'eghdam.html')



def SendSmsReset(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        phone = request.POST.get('phone')
        if MyUser.objects.filter(phone=phone):
            MyUser.objects.filter(phone=phone).update(token=number)
        else:
            return HttpResponse("شما اکانتی ندارید")
    api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
    params = {'sender' : '10000080808880', 'receptor': f'{phone}', 'message' :f'{number}' }
    api.sms_send( params)
    response = render(request,'verify2.html')
    x =phone
    response.set_cookie('phone_number_cookie',x,1000)
    return response 


def ResetProfileView(request):
    return render(request,'ResetPasswordView.html',{})

def ResetProfile(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        password = request.POST.get('password')
        phone_c = request.COOKIES['phone_number_cookie']
        MyUser.objects.filter(phone=phone_c).update(
            password=make_password(password)
        )
        return HttpResponse("Done")


def VerifyChecked2(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        try :
            user = MyUser.objects.get(phone= phone_c)
        except:
            return HttpResponse('error')
        if user.token == token :
            return render(request,'ResetPasswordView.html')
        else :
            return HttpResponse('error 2')