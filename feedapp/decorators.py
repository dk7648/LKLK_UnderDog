from django.http import HttpResponseForbidden

from feedapp.models import Feed


def feed_ownership_required(func):
    def decorated(request, *args, **kwargs):
        feed = Feed.objects.get(pk=kwargs['pk'])
        if not feed.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated