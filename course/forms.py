# Imports
from django import forms
from .models import Course
from django.core.exceptions import ValidationError


# Form add foto
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}


    # Validate fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 0:
            raise ValidationError('Поле Название курса не должно быть пустым.')
        else:
            return name


    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) <= 5:
            raise ValidationError('Слишком мало символов для описания курса. Опишите его подробнее.')
        else:
            return description