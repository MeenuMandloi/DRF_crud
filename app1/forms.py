from django import forms
from app1.models import Details


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"