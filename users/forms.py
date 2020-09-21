from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile
from pages.models import Post

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ProfielUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['front','back','about','desc']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title']