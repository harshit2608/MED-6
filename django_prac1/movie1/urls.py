from django.conf.urls import url
from .views import index,detail

app_name='movie1'

urlpatterns=[
    url('',index,name="index"),
    url(r'^(?P<movie_id>[0-9]+)/$',detail,name='detail'),
]