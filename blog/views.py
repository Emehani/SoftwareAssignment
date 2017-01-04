from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import BlogForm
from tags.models import Tag
from .models import Blog


def show_blog(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "get_blog.html", {"blogs": Blog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all(),
                                             "form": form})




def get_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "show_blog.html", {"blog": blog})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")



@permission_required('is_superuser')
def show_all_blog(request):
    return render(request, "get_blog.html", {"blogs": Blog.objects.all()})

@permission_required('is_superuser')
def show_all_blog_from_user(request, userId):
    return render(request, "get_blog.html", {"blogs": Blog.objects.filter(owner=userId)})










