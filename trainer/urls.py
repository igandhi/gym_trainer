from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^routine_detail/(?P<random_url>[-\w]+)/$', views.routine_detail, name="routine_detail")
]
