from django.shortcuts import render
from blog.models import Blog, Category
from assignments.models import About, SocialLink


def home(request):

    categories = Category.objects.all()

    featured_posts = Blog.objects.filter(
        is_featured=True,
        status='Published'
    )

    posts = Blog.objects.filter(
        status='Published'
    ).order_by('-created_at')

    about = About.objects.first()

    social_links = SocialLink.objects.all()

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        'social_links': social_links,
    }

    return render(request, 'home.html', context)