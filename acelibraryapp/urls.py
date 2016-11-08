from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.member_login, name='member_login'),
    url(r'^home/', views.home, name='home'),
    #TODO : Add routes for other pages
]
