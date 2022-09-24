from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почта'}),
            'website': forms.TextInput(attrs={'placeholder': 'Веб-сайт'}),
            'message': forms.Textarea(attrs={'placeholder': 'Комментарий'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text_input_form'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'text_input_form'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_input_form'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'text_input_form'}))
    field_order = ('username', 'email', 'password1', 'password2')

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text_input_form'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_input_form'}))
