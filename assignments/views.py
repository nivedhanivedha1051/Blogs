from blog.models import Blog

def search(request):
    keyword = request.GET.get('keyword', '').strip()

    posts = Blog.objects.filter(title__icontains=keyword)

    print("SEARCH KEYWORD:", keyword)
    print("SEARCH RESULTS:", posts)

    context = {
        'posts': posts,
        'keyword': keyword,
    }

    return render(request, 'search.html', context)