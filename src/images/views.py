from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, RedirectView, DetailView, FormView

from .forms import ImageForm, CommentForm
from .models import Image, Comment


class IndexView(ListView):
    model = Image
    context_object_name = 'images'
    extra_context = {'form': ImageForm()}
    template_name = 'images/index.html'
    paginate_by = 3
    ordering = '-id'


class AddImageView(LoginRequiredMixin, CreateView):
    login_url = 'authorization:login'
    model = Image
    fields = ['image', 'signature']
    success_url = reverse_lazy('images:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LikeView(LoginRequiredMixin, RedirectView):
    login_url = 'authorization:login'

    def get(self, *args, **kwargs):
        image = Image.objects.get(id=self.kwargs['pk'])

        if image.likes.filter(id=self.request.user.id).exists():
            image.likes.remove(self.request.user)
        else:
            image.likes.add(self.request.user)

        return JsonResponse({'likes': image.likes.count()})


class ImageView(DetailView):
    template_name = 'images/comments.html'
    model = Image
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        kwargs['form'] = CommentForm
        return super().get_context_data(**kwargs)


class AddCommentView(LoginRequiredMixin, FormView):
    login_url = 'authorization:login'
    form_class = CommentForm

    def form_valid(self, form):
        form.save(self.request.user, self.kwargs['pk'])
        return JsonResponse({'username': self.request.user.username})


class GetCommentsView(RedirectView):
    def get(self, *args, **kwargs):
        comments = Comment.objects.filter(image=Image.objects.get(pk=kwargs['pk']))
        data = {}

        for comment in comments:
            data[comment.id] = {}
            data[comment.id]['author'] = comment.author.username
            data[comment.id]['text'] = comment.text

        return JsonResponse({'comments': data})
