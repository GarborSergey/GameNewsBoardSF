from django import forms
from .models import UserProfile


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Firs Name', max_length=85, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    avatar = forms.ImageField(label='Avatar', required=False)


class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()