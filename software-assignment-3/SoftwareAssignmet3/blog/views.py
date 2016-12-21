from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import Bloog

# Create your views here.
def show_blog(request):

    return render(request, "get_blog.html", {"blogs": Bloog.objects.all()})


def get_blog(request, blog_id):
    try:
        blog = Bloog.objects.get(id=blog_id)
        return render(request, "show_blog.html", {"blog": blog})
    except Bloog.DoesNotExist:
        raise Http404("We don't have any.")