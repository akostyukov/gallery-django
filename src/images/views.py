from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import ListView, CreateView, RedirectView

from .forms import ImageForm
from .models import ImageModel


class ImageView(ListView):
    model = ImageModel
    context_object_name = 'images'
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

    def get_redirect_url(self, *args, **kwargs):
        image = ImageModel.objects.get(id=self.kwargs['pk'])

        if image.likes.filter(id=self.request.user.id).exists():
            image.likes.remove(self.request.user)
        else:
            image.likes.add(self.request.user)

        return reverse_lazy('images:index')

# class LikeView(LoginRequiredMixin, RedirectView):
#     login_url = 'authorization:login'
#
#     def get_redirect_url(self, *args, **kwargs):
#         image = ImageModel.objects.get(id=self.kwargs['pk'])
#
#         if image.likes.filter(id=self.request.user.id).exists():
#             image.likes.remove(self.request.user)
#         else:
#             image.likes.add(self.request.user)
#
#         return reverse_lazy('images:index')
