from django.shortcuts import render ,redirect       
from django.http import HttpResponse
from django.contrib.auth.models import User,auth  
from django.contrib import messages
from .models import Profile
def index(request):    
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password 2')

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')