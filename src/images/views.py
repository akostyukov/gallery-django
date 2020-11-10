from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ImageForm
from .models import ImageModel


class Image(View):
    def get(self, request):
        return render(request, 'images/index.html', {'form': ImageForm(), 'images': ImageModel.objects.all()})

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            ImageModel.objects.create(image=form['image'].value(), signature=form['signature'].value())

        return redirect('images:index')
