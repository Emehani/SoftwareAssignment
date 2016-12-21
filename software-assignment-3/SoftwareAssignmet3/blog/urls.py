from django.conf.urls import url

from blog.views import show_blog, get_blog

urlpatterns = [
    url(r'^$', show_blog),
    url(r'^(?P<blog_id>[0-9]+)', get_blog)
]