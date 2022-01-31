from django.shortcuts import render
from blog.models import Post


posts = [
    {
        'author': 'JayThree',
        'title': 'Blog Post 1',
        'content': 'Blog 1 Content!',
        'date_posted': 'January 20, 2022'
    },
    {
        'author': 'JayThree',
        'title': 'Blog Post 2',
        'content': 'Blog 2 Content!',
        'date_posted': 'January 23, 2022'
    }
]


def home(request):

    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
