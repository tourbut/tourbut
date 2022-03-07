
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_requried(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not (article.writer == request.user):
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated