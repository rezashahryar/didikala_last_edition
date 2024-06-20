from django import forms
from django.db.models import Q

from .models import User, ActivationViaEmail

# create your forms here

class RegisterForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['password']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(Q(mobile=username) | Q(email=username))
            raise forms.ValidationError("کاربری از قبل با این ایمیل یا موبایل درسایت موجود است")
        except User.DoesNotExist:
            ...
        
        return username


class LoginForm(forms.ModelForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(Q(mobile=username) | Q(email=username))
        except User.DoesNotExist:
            raise forms.ValidationError("کاربری با این ایمیل یا موبایل در سیستم ثبت نیست")
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(Q(mobile=username) | Q(email=username))
            if not user.check_password(password):
                raise forms.ValidationError("پسورد وارد شده اشتباه است")
        except User.DoesNotExist:
            ...
        
        return password
