from django.conf.urls import url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index')
]