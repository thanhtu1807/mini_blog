from django.shortcuts import render
from .models import Blog, Blogger, Comment
from django.views import generic
# Create your views here.


def index(request):
    num_blogs = Blog.objects.count()
    num_bloggers = Blogger.objects.count()
    num_comments = Comment.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_comments': num_comments,
    }

    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

    # def get_queryset(self):
    #     return Blog.objects.all().order_by('-post_date')

class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger