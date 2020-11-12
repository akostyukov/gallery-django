from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from src.authorization.forms import UserForm


class RegisterView(TemplateView):
    template_name = 'registration/register.html'
    extra_context = {'form': UserForm}


class CreateUser(FormView):
    form_class = UserForm
    success_url = reverse_lazy('authorization:login')

    def form_valid(self, form):
        user = User.objects.create_user(username=form['username'].value())
        user.set_password(form['password'].value())
        user.save()

        return redirect(self.get_success_url())
