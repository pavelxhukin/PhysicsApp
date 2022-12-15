from .models import FizProperties
from django.forms import ModelForm, TextInput, Textarea

class FizPropertiesForm(ModelForm):
    class Meta:
        model = FizProperties
        fields = ["title","field1","field2","field3","field4","field5","field6",
                  "field7","field8","field9","field10","field11","field12","field13","field14"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write title'
            }),
            "field1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field1'
            }),
            "field2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field2'
            }),
            "field3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field3'
            }),
            "field4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field4'
            }),
            "field5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field5'
            }),
            "field6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field6'
            }),
            "field7": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field7'
            }),
            "field8": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field8'
            }),
            "field9": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field9'
            }),
            "field10": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field10'
            }),
            "field11": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field11'
            }),
            "field12": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field12'
            }),
            "field13": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field13'
            }),
            "field14": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write field14'
            })
        }