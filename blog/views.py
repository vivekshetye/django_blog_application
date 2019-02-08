from django.shortcuts import render


posts = [
    {
        'author' : 'Vivek Shetye',
        'title' : 'Blog Post 1',
        'content' : 'First blog post content',
        'date' : 'Feb 6 2019'
    },
    {
        'author' : 'Vivek Shetye',
        'title' : 'Blog Post 2',
        'content' : 'Second blog post content',
        'date' : 'Feb 6 2019'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
