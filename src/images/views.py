from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ImageForm
from .models import ImageModel


class ImageView(ListView):
    model = ImageModel
    context_object_name = 'images'
    extra_context = {'form': ImageForm()}
    template_name = 'images/index.html'
    paginate_by = 3
    ordering = '-id'


class AddImage(CreateView):
    model = ImageModel
    fields = ['image', 'signature']
    success_url = reverse_lazy('images:index')
