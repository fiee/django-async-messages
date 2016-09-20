from django.conf.urls.defaults import url
from test.views import index

urlpatterns = [
    url(r'^$', index),
]
