from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField(required=True)
    signature = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Описание к фото'}))


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200)
