from django.conf.urls import url

# from bos.apps.users.views import CreateUser
from bos.apps.users.views import CreateUser, Faltu

urlpatterns = [
    # url('', views.CreateUser.as_view(), name='create-user'),
    url('^$', Faltu.as_view(), name='edit-user'),
    url('^create/$', CreateUser.as_view(), name='create-user'),
]
