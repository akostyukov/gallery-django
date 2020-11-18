from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, FormView

from .forms import ImageForm
from .models import ImageModel


class ImageView(ListView):
    model = ImageModel
    context_object_name = 'images1'
    extra_context = {'form': ImageForm()}
    template_name = 'images/index.html'
    paginate_by = 3
    ordering = '-id'


@method_decorator(login_required, name='dispatch')
class AddImage(FormView):
    form_class = ImageForm
    success_url = reverse_lazy('images:index')

    def form_valid(self, form):
        ImageModel.objects.create(image=form['image'].value(),
                                  signature=form['signature'].value(),
                                  user=self.request.user)
        return redirect(self.get_success_url())
