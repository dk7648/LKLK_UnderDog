from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, hello

app_name = "accountapp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    #추후 만들 마이페이지, 비밀번호 바꾸기, 계정 삭제
    #path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    #path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    path('hello/', hello, name='hello')
]