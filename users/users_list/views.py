from django.shortcuts import render
from users_list.models import UserBasic, UserProfileInfo
from . import forms
from users_list.forms import FormUser, UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    my_dict = {'valor': 'Where do you wanna go folk?'}
    return render(request,'users_list/index.html', context = my_dict)

def users(request):

    user_li = UserProfileInfo.objects.order_by('user')
    user_dict = {'users': user_li}

    return render(request,'users_list/users.html', context=user_dict)

def register(request):
    registered = False

    if request.method == 'POST':

        # Here we grab the information of the form y theses two variables
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'users_list/registration.html',
                    {'form_user': user_form,
                        'form_profile': profile_form,
                        'registered': registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') #Here we're grabbing the input with the name = username in the login.html
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Username: {} and password: {} are not valid".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'users_list/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def form_user_view(request):
    # Here starts ModelForm
    form= FormUser()

    if request.method == "POST":
        form = FormUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error")

    return render(request, 'users_list/form_page.html', {'form':form})
