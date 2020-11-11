from django import forms

from .models import ImageModel


class ImageForm(forms.Form):
    image = forms.ImageField(required=True)
    signature = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Описание к фото'}))

    def save(self):
        ImageModel.objects.create(image=self['image'].value(), signature=self['signature'].value())
