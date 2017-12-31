from django.conf.urls import url

# from bos.apps.users.views import CreateUser
from bos.apps.users.views import CreateUser, Login, SignUp, Dashboard

urlpatterns = [
    # url('', views.CreateUser.as_view(), name='create-user'),
    # url('^$', Faltu.as_view(), name='edit-user'),
    url('^create/$', CreateUser.as_view(), name='create-user'),
    url('signup/', SignUp.as_view(), name='signup'),
    url('^dashboard/$', Dashboard.as_view(), name='user-dashboard'),
    # url('^login/$', Login.as_view(), name='login'),
]
