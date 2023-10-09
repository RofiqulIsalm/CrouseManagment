from django import forms
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

DEV_TYPE_CHOICES = (
    ('frontend', 'Frontend Developer'),
    ('backend', 'Backend Developer'),
    ('fullstack', 'Fullstack Developer'),
    ('wordpress', 'Wordpress Developer'),
)