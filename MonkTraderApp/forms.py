from decimal import Decimal
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, MarketReport, SignalService, Education
from dal import autocomplete  # Importing Django Autocomplete Light for autocomplete fields

# Custom user creation form that extends Django's UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Specify the model to use
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # Fields to include in the form

# Custom authentication form that extends Django's AuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Specify the model to use
        fields = ['username', 'password']  # Fields to include in the form

# Form for creating or updating a market report
class MarketReportForm(forms.ModelForm):
    class Meta:
        model = MarketReport  # Specify the model to use
        fields = ['title', 'report', 'author']  # Fields to include in the form
        exclude = ['author']  # Exclude the author field from the form (set automatically)

# Form for creating or updating a signal service
class SignalServiceForm(forms.ModelForm):
    class Meta:
        model = SignalService  # Specify the model to use
        fields = ['asset', 'bias', 'entry', 'SL', 'TP']  # Fields to include in the form
        widgets = {
            'asset': autocomplete.ListSelect2(url='asset-autocomplete')  # Use autocomplete for the asset field
        }

# Form for uploading educational content
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education  # Specify the model to use
        fields = ['title', 'file']  # Fields to include in the form
        