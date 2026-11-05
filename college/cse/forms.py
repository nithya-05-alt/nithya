from django import forms
from cse.models import students
class StudentsForm(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'