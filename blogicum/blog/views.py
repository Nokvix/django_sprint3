from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Category
from django.utils import timezone


# posts = []
#
# posts_dict = {}
# for post in posts:
#     if post['id'] not in posts_dict:
#         posts_dict[post['id']] = post


def index(request):
    post_list = (Post.objects
                 .select_related('category', 'location')
                 .filter(Q(created_at__lt=timezone.now())
                         & Q(is_published__exact=True)
                         & Q(category__is_published__exact=True))
                 .order_by('-created_at')[:5])

    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = posts_dict.get(post_id)

    if not post:
        raise Http404(f'Поста с идентификатором {post_id} нет')
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404

    post_list = (Post.objects.select_related('category', 'location')
                 .filter(category__slug__exact=category_slug,
                         is_published__exact=True,
                         created_at__lt=timezone.now()))

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
