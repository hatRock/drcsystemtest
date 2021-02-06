from django import forms
from .models import Profile


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['email', 'mobile', 'primary_email', 'user']
