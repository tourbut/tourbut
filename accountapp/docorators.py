from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_requried(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not (user == request.user):
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated