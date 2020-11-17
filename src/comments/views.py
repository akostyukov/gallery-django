from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView

from images.models import ImageModel

from .forms import CommentForm
from .models import Comment


class ImageView(DetailView):
    template_name = 'comments/index.html'
    model = ImageModel
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        kwargs['comments'] = Comment.objects.filter(image=ImageModel.objects.get(pk=self.kwargs['pk']))
        kwargs['form'] = CommentForm
        return super().get_context_data(**kwargs)


class SubmitCommentView(LoginRequiredMixin, CreateView):
    login_url = 'authorization:login'
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.image = ImageModel.objects.get(pk=self.kwargs['pk'])

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comments:image', args=(self.kwargs['pk']))
