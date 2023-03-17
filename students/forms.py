from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms.widgets import DateInput, PasswordInput, NumberInput


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        try:
            self.fields['username'].label = "Phone Number"
            self.fields['password'].label = "Password (Paste Any Garbage Value)"
        except:
            pass
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CourseForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ['name']
        model = Course

class BatchForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)
    
    class Meta:
        fields = '__all__'
        model = Batch
        widgets = {
            'opening_date': DateInput(attrs={'type': 'date'}),
            'closing_date': DateInput(attrs={'type': 'date'}),
        }

class StudentForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields.pop('applying_for')
        self.fields.pop('describe_queries')
    
    class Meta:
        fields = '__all__'
        model = Student
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            # 'closing_date': DateInput(attrs={'type': 'date'}),
        }

class StaffForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ['first_name','last_name','username','password']
        model = User
        widgets = {
            'password': PasswordInput(attrs={'type': 'password'}),
            'username': NumberInput(attrs={'type': 'number'}),
            # 'closing_date': DateInput(attrs={'type': 'date'}),
        }





