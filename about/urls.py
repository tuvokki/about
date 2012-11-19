from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from about.models import About

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=About.objects.order_by('-pub_date')[:1],
            context_object_name='latest_about_list',
            template_name='about/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
        	model=About,
            template_name='about/detail.html')),
#    url(r'^$', 'index'),
#    url(r'^(?P<about_id>\d+)/$', 'about.views.detail'),
)
