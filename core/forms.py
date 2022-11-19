from django import forms

from core.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = {'id'}
        widgets = {
            "type": forms.widgets.CheckboxSelectMultiple(),
            "age": forms.widgets.NumberInput(attrs={"class": "form-control mb-3"}),
            "email": forms.widgets.EmailInput(attrs={"class": "form-control mb-3"}),
            "name": forms.widgets.TextInput(attrs={"class": "form-control mb-3"}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).count() > 0:
            raise forms.ValidationError("This email does exist")
        return email

