from django.shortcuts import render

posts = [
    {
        'author':'Ivan',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted': 'January 07,2019',
    },
        {
        'author':'Ivan2',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'Tomorrow',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})