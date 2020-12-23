from django import forms

from .models import Comment, Image


class ImageForm(forms.Form):
    image = forms.ImageField(required=True)
    signature = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Описание к фото'}))


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200)

    def save(self, user, image_id):
        Comment.objects.create(text=self['text'].value(), author=user, image=Image.objects.get(pk=image_id))
