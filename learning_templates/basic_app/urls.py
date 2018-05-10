from django.conf.urls import include, url
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative_url_templates/$', views.relative_url_templates, name='relative_url_templates'),
    url(r'^other/$', views.other, name='other'),
]
