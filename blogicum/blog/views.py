from django.shortcuts import render
from django.http import Http404


posts_dict = {}
for post in posts:
    if post['id'] not in posts_dict:
        posts_dict[post['id']] = post


def index(request):
    context = {
        'posts': posts[::-1],
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
    context = {
        'category_slug': category_slug,
    }
    return render(request, 'blog/category.html', context)
