from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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


@method_decorator(login_required, name='dispatch')
class AddImage(CreateView):
    model = ImageModel
    fields = ['image', 'signature']
    success_url = reverse_lazy('images:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def like(request, image_id):
    image = ImageModel.objects.get(id=image_id)

    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
    else:
        image.likes.add(request.user)
    return redirect('images:index')
