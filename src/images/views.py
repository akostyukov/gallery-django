from django.shortcuts import redirect
from django.views.generic import ListView, FormView

from .forms import ImageForm
from .models import ImageModel


class ImageView(ListView):
    model = ImageModel
    context_object_name = 'images'
    extra_context = {'form': ImageForm()}
    template_name = 'images/index.html'


class AddImage(FormView):
    form_class = ImageForm
    template_name = 'images/index.html'
    success_url = 'images:index'

    def form_valid(self, form):
        ImageModel.objects.create(image=form['image'].value(), signature=form['signature'].value())
        return redirect(self.get_success_url())
