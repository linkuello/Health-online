from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Categories
from .forms import PostForm, CommentForm
from blog import models
from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view(request):
    categories = Categories.objects.all()
    posts = Post.objects.all().order_by('-published', )
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST, request.FILES)
    post_form = PostForm()
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()

    context = {
        'posts': posts,
        'common_tags': common_tags,
        'form': form,
        'categories': categories,
    }
    return render(request, 'blog/home.html', locals())


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            # return redirect('detail_view', slug=post.slug)
            return HttpResponseRedirect('/blog/post/{}/'.format(post.slug))
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def homepage(request):
    posts = Post.objects.all().filter(category='3').order_by('-published', )
    common_tags = Tag.objects.all()
    form_c = CommentForm()

    try:
        post_slug = request.POST['slug']
        comment_name = request.POST['name']
        comment_email = request.POST['email']
        comment_body = request.POST['body']
    except:
        post_slug = None
        message = "Error"

    if request.method == 'POST' and post_slug is not None:
        post = models.Post.objects.get(slug=post_slug)
        comment_post = models.Comment.objects.create(post=post, name=comment_name, body=comment_body, email=comment_email)
        comment_post.save()

    return render(request, 'blog/nutrition.html', locals())


def blog_sport(request):
    posts = Post.objects.all().filter(category='1').order_by('-published', )
    common_tags = Tag.objects.all()
    form_c = CommentForm()

    try:
        post_slug = request.POST['slug']
        comment_name = request.POST['name']
        comment_email = request.POST['email']
        comment_body = request.POST['body']
    except:
        post_slug = None
        message = "Error"

    if request.method == 'POST' and post_slug is not None:
        post = models.Post.objects.get(slug=post_slug)
        comment_post = models.Comment.objects.create(post=post, name=comment_name, body=comment_body, email=comment_email)
        comment_post.save()

    return render(request, 'blog/sport.html', locals())


def blog_weight_lost(request):
    posts = Post.objects.all().filter(category='2').order_by('-published', )
    common_tags = Tag.objects.all()
    form_c = CommentForm()

    try:
        post_slug = request.POST['slug']
        comment_name = request.POST['name']
        comment_email = request.POST['email']
        comment_body = request.POST['body']
    except:
        post_slug = None
        message = "Error"

    if request.method == 'POST' and post_slug is not None:
        post = models.Post.objects.get(slug=post_slug)
        comment_post = models.Comment.objects.create(post=post, name=comment_name, body=comment_body, email=comment_email)
        comment_post.save()

    return render(request, 'blog/weight_lost.html', locals())


def test(request):
    categories = Categories.objects.all()
    posts = Post.objects.all().order_by('-published', )
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST, request.FILES)
    post_form = PostForm()
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()
    # else:
    #     c_t = request.POST['title']
    #     c_d = request.POST['description']
    #     c_c = request.POST['content']
    #     c_t = request.POST['tags']

    context = {
        'posts': posts,
        'common_tags': common_tags,
        'form': form,
    }

    return render(request, 'blog/Blog_test.html', locals())
