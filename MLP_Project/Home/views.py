from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact,Notice
from django.contrib import messages
import json
from django.http import JsonResponse
import pytesseract
import requests
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    if request.method == 'POST':
        notice_text = request.POST.get('notice')
        notice = Notice(text=notice_text)
        notice.save()
        messages.success(request, 'Notice added successfully.')
    
    notices = Notice.objects.all()
    try:
        user_id = request.session.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        return render(request, 'index.html', {'notices': notices, 'user': user})
    except User.DoesNotExist:
        return render(request,'index.html',{'notices': notices})

def add_notice(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print("Message --------------> :",message)
        notice = Notice.objects.create(message=message)
        # Perform any additional processing or validation as needed
        notice.save()
        notices = Notice.objects.all()
        user_id = request.session.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        print("Add Notice :", request.user)
        # return render(request, 'index.html', {'user': request.user, 'notices': notices})
        return render(request, 'index.html', {'user': user, 'notices': notices})
    return render(request, 'index.html', {'user': user, 'notices': notices})

def edit_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        print("Message Received after editing:",message)
        notice.message = message
        notice.save()
        user_id = request.session.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        return render(request, 'index.html', {'user': user, 'notices': Notice.objects.all})
    return render(request, 'edit_notice.html', {'notice': notice})

def delete_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.delete()
    user_id = request.session.get('user_id')
    user = get_user_model().objects.get(id=user_id)
    return render(request, 'index.html', {'user': user, 'notices': Notice.objects.all})

def contactUs(request):
    if request.method=="POST":
        # Request.POST gives the dictionary
        email=request.POST.get('email')
        text=request.POST.get('text')
        date=datetime.now()
        contact=Contact(email=email,text=text,date=date)
        contact.save()
        messages.success(request, 'Profile details updated.')
    try:
        user_id = request.session.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        return render(request,'contactUs.html',{'user':user})
    except User.DoesNotExist:
        return render(request,'contactUs.html')

def aboutus(request):
    try:
        user_id = request.session.get('user_id')
        user = get_user_model().objects.get(id=user_id)
        return render(request,'aboutus.html',{'user':user})
    except User.DoesNotExist:
        return render(request,'aboutus.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    remember_me = request.POST.get('remember') 
    print(f"Username:{username}")
    print(f"Password:{password}")
    user=authenticate(username=username,password=password)
    print(user)
    if user is not None:
        if remember_me:
                # Set session expiry to a longer duration (e.g., 30 days)
                request.session.set_expiry(2592000)
        
        # Store the user ID in the session
        request.session['user_id'] = user.id       
        notices = Notice.objects.all()
        print("Log in :", user)
        return render(request, 'index.html', {'user': user, 'notices': notices, 'success': True})
    return render(request,'login.html',{'error': True})


def loginlogoutbutton(request):
    if request.method == 'POST':
        # Handle button click
        if 'loginbutton' in request.POST:
            # Do something when button1 is clicked
            print("Login")
            return render(request,'login.html')
        else:
            # Do something when button2 is clicked
            logout(request)
            notices = Notice.objects.all()
            return render(request, 'index.html', {'user': request.user, 'notices': notices, 'success': True})
           

def registeration(request):
    if request.method=='POST':
        print("Inside Registeration")
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print("username :",username)
        print("Password :",password)
        print("Email :",email)
        # Create a new user
        user = User.objects.create_user(username=username,
                                email=email,
                                password=password)
        return render(request,'login.html')
        # Save the user to the database
        user.save()
    return render(request,'registeration.html')

def summaryhistory(request):
    return render(request,'summaryhistory.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = '/password_reset/done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/reset/done/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Retrieve the email entered by the user
        # Perform further processing or send the email using the email address
        print("Email ------------",email)
        # Example: Sending a password reset email using Django's built-in PasswordResetView
        password_reset_view = CustomPasswordResetView.as_view()
        return password_reset_view(request)
    
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    password_reset_confirm_view = CustomPasswordResetConfirmView.as_view()
    return password_reset_confirm_view(request, uidb64=uidb64, token=token)

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')
