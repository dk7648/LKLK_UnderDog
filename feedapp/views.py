from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from feedapp.decorators import feed_ownership_required
from feedapp.forms import FeedCreationForm
from feedapp.models import Feed


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FeedCreateView(CreateView):
    model = Feed
    form_class = FeedCreationForm
    template_name = 'feedapp/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('feedapp:detail', kwargs={'pk': self.object.pk})

class FeedDetailView(DetailView):
    model = Feed
    context_object_name = 'target_post'
    template_name = 'feedapp/detail.html'



@method_decorator(feed_ownership_required, 'get')
@method_decorator(feed_ownership_required, 'post')
class FeedUpdateView(UpdateView):
    model = Feed
    context_object_name = 'target_post'
    form_class = FeedCreationForm
    template_name = 'feedapp/update.html'

    def get_success_url(self):
        return reverse('feedapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(feed_ownership_required, 'get')
@method_decorator(feed_ownership_required, 'post')
class FeedDeleteView(DeleteView):
    model = Feed
    context_object_name = 'target_post'
    success_url = reverse_lazy('feedapp:list')
    template_name = 'feedapp/delete.html'

class FeedListView(ListView):
    model = Feed
    context_object_name = 'post_list'
    template_name = 'feedapp/list.html'
    paginate_by = 25
