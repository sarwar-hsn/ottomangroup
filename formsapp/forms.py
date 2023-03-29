from django import forms

from .models import Education, Consultancy, Contact
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude=('created',)
        widgets = {
            'preferred_department': forms.TextInput(attrs={
                'placeholder':'e.g: aviation engineering'
            }),
            'date_of_birth': DatePickerInput(),
            'message': forms.Textarea(attrs={'rows':3}),
        }

class ConsultancyForm(forms.ModelForm):
    TimePickerInput._date_format = "%H:%M"
    TimePickerInput.backend_date_format = "HH:mm"
    class Meta:
        model = Consultancy
        fields = [
            'full_name',
            'email',
            'whatsapp',
            'country',
            'date',
            'time',
            'message',
        ]
        labels={
            'date':('Date you want to meet'),
            'time':('Scheduled time'),
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'your full name'}) ,
            'date' : DatePickerInput(options={"format": "MM/DD/YYYY"}),
            'time' : TimePickerInput(),
            'email': forms.TextInput(attrs={'placeholder':'your email address'}),
            'country': forms.TextInput(attrs={'placeholder':'country of residence'}),
            'whatsapp': forms.TextInput(attrs={'placeholder':'your whatsapp number'}),
            'message': forms.Textarea(attrs={'rows':3}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created',)

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'your full name'}) ,
            'email': forms.TextInput(attrs={'placeholder':'your email address'}),
            'whatsapp': forms.TextInput(attrs={'placeholder':'whatsapp number with country code'}),
            'message': forms.Textarea(attrs={'rows':3}),
        }