import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, RedirectView

from .forms import ImageForm
from .models import ImageModel


class ImageView(ListView):
    model = ImageModel
    context_object_name = 'images1'
    extra_context = {'form': ImageForm()}
    template_name = 'images/index.html'
    paginate_by = 3
    ordering = '-id'


class AddImage(LoginRequiredMixin, CreateView):
    login_url = 'authorization:login'
    model = ImageModel
    fields = ['image', 'signature']
    success_url = reverse_lazy('images:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LikeView(LoginRequiredMixin, RedirectView):
    login_url = 'authorization:login'

    def get(self, *args, **kwargs):
        image = ImageModel.objects.get(id=self.kwargs['pk'])

        if image.likes.filter(id=self.request.user.id).exists():
            image.likes.remove(self.request.user)
            image_url = '/static/images/icons/like_unset.png'
        else:
            image.likes.add(self.request.user)
            image_url = '/static/images/icons/like_set.png'

        data = {'likes': image.likes.count(), 'image_url': image_url}
        return HttpResponse(json.dumps(data), content_type='application/json')
