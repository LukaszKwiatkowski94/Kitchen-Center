from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from customuser.models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use.')

