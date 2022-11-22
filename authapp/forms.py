from authapp.models import AppUser, Course
from django.contrib.auth.forms import UserCreationForm
from django import forms


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ['username', 'course']

    def __init__(self, *args, **kwargs):
        super(AppUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ModelChoiceField(queryset=Course.objects.all())
