from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^entrar/$', login,
        {'template_name':'accounts/login.html'}, name='login'),
    url(r'^cadastre-se/$', views.register, name='register'),

]