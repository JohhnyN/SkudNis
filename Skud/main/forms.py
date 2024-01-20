from django import forms
from .models import *


class AddCardHistory(forms.Form):
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        label="Преподаватель",
        empty_label="Выберите учителя",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    office = forms.ModelChoiceField(
        queryset=Office.objects.all(),
        label="Кабинет",
        empty_label="Выберите кабинет",
        widget=forms.Select(attrs={"class": "form-control"}),
    )


class ReturnCardHistory(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].empty_label = 'Выберите учителя'
        self.fields['office'].empty_label = 'Выберите кабинет'
        
    class Meta:
        model = CardHistory
        fields = ["teacher", "office", "end_time", "returned"]
        widgets = {
            "teacher": forms.Select(attrs={"class": "form-control"}),
            "office": forms.Select(attrs={"class": "form-control"}),
        }
