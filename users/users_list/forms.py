from django import forms
from django.core import validators
from users_list.models import UserBasic
from users_list.models import UserProfileInfo
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
    # This following code was for forms.forms
    # name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.CharField()
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])
    # Here start code for ModelForm
    class Meta():
        model = UserBasic
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
