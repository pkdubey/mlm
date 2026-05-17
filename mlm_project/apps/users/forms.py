from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'})
    )
    referral_code = forms.CharField(
        max_length=20,
        required=False,
        label='Sponsor Referral Code',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sponsor code (optional)'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2', 'referral_code']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Create password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    def clean_referral_code(self):
        code = self.cleaned_data.get('referral_code')
        if code:
            if not User.objects.filter(referral_code=code).exists():
                raise forms.ValidationError('Invalid referral code.')
        return code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        code = self.cleaned_data.get('referral_code')
        if code:
            user.sponsor = User.objects.get(referral_code=code)
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'email']
