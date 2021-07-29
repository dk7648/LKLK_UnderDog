from django.urls import path

from feedapp.views import FeedCreateView, FeedUpdateView, FeedDetailView, FeedListView, FeedDeleteView

app_name = "feedapp"

urlpatterns = [
    path('create/', FeedCreateView.as_view(), name='create'),
    path('update/<int:pk>', FeedUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', FeedDetailView.as_view(), name='detail'),
    path('list/', FeedListView.as_view(), name='list'),
    path('delete/<int:pk>', FeedDeleteView.as_view(), name='delete'),
]