from django import forms

from . import models


class LogoutForm(forms.Form):
    pass


class CompanyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Company


class FamilyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Family
