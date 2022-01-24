from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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
    # return HttpResponse(' ')

    # template = loader.get_template('blog/home.html')
    # context = {}
    # return HttpResponse(template.render(context, request))

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>About Page</h1>')

    # template = loader.get_template('blog/about.html')
    # context = {}
    # return HttpResponse(template.render(context, request))

    return render(request, 'blog/about.html', {'title': 'About'})
