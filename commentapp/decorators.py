
from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_requried(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not (comment.writer == request.user):
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated