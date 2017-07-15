from django import forms
from .models import ImgAdd

class AddImgForm(forms.ModelForm):
    class Meta:
        model = ImgAdd
        fields = ('title', 'img')
