from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^registro/$', views.registro_usuario, name='registro_usuario'),
    url(r'^gracias/(?P<username>[\w]+)/$', views.gracias, name='gracias'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
