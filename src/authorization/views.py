from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import UserForm


class Login(LoginView):
    pass


class Logout(LogoutView):
    pass


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserForm
    success_url = reverse_lazy('authorization:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('images:index')
        return super().get(request, *args, **kwargs)
