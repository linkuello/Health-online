from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def home_view(request):
    posts = Post.objects.all().order_by('-published',)
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()

    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'blog/home.html', context)

def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method =="POST":
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
        'post':post,
        'form':form,
    }
    return render(request, 'blog/detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blog/home.html', context)


def homepage(request):
    posts = Post.objects.all().order_by('-published',)
    common_tags = Tag.objects.all()

    context = {
        'posts': posts,
        'common_tags': common_tags,

    }
    return render(request, 'blog/index.html', locals())


def test(request):
    all_tags = Tag.objects.all()
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.all()
    form = PostForm(request.POST)
    post_form = PostForm()
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()
    else:
        c_t = request.POST['title']
        c_d = request.POST['description']
        c_c = request.POST['content']
        c_t = request.POST['tags']


    context = {
        'posts': posts,
        'common_tags': common_tags,
        'form': form,
    }

    return render(request, 'blog/Blog_test.html', locals())
