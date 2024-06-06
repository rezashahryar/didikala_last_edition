from django import forms
from .models import UsersEmail

# create your forms here

class UserEmailForm(forms.ModelForm):

    class Meta:
        model = UsersEmail
        fields = ['email']
