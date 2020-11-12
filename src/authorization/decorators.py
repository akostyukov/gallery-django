from django.shortcuts import redirect


def authorized(func):
    def wrapped(request):
        if request.user.is_authenticated:
            return redirect('images:index')
        else:
            return func(request)
    return wrapped
