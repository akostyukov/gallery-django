from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from images.models import ImageModel

from .forms import CommentForm
from .models import Comment


class ImageView(DetailView):
    template_name = 'comments/index.html'
    model = ImageModel
    extra_context = {'comments': Comment.objects.get(image=model.id), 'form': CommentForm}
    context_object_name = 'image'


class SubmitCommentView(CreateView):
    model = Comment
    fields = ['text']
    success_url = reverse_lazy('comments:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.image = ImageModel.objects.get(pk=self.kwargs['pk'])

        return super().form_valid(form)
