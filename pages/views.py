from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .models import Skill
from .models import ContactMessage
from .forms import ContactForm


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'pages/blog_detail.html', {'post': post} )

def portfolio(request):
    skills = Skill.objects.all()
    return render(request, 'pages/portfolio.html', {'skills': skills})

def portfolio_detail(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    return render(request, 'pages/portfolio_detail.html', {'skill': skill})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you, your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
