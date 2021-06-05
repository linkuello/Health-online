from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Categories, Likes
from blog.forms import CommentForm
from blog import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from calories.forms import CreateUserForm
from django.contrib import messages


def homepage(request):
    if request.user is not None:
        user = request.user
        username = user.username

    blog_posts = Post.objects.all().filter(enabled=True).order_by('-published',)[:3]
    form_c = CommentForm()

    try:
        post_slug = request.POST['slug']
        comment_name = request.POST['name']
        comment_email = request.POST['email']
        comment_body = request.POST['body']
    except:
        post_slug = None

    if request.method == 'POST' and post_slug is not None:
        post = models.Post.objects.get(slug=post_slug)
        comment_post = models.Comment.objects.create(post=post, name=comment_name, body=comment_body,
                                                     email=comment_email)
        comment_post.save()

    return render(request, 'main_homepage.html', locals())


@login_required(login_url='login')
def like(request, slug):
    user = request.user
    post = get_object_or_404(Post, slug=slug)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return redirect('homepage')


def LoginPage(request, page=''):
    if request.user.is_authenticated:
        return redirect(page)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                if page == '':
                    return redirect('homepage')
                else:
                    return redirect(page)
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'login/login.html', context)



def LogOutPage(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account was created for "+ user)
                return redirect('login')

        context = {'form':form}

        return render(request, 'login/register.html', context)
