from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from .models import UsrPost, UsrReg,LikePost
from .forms import RegistrationForm, SignUpForm, PostForm, ChangeForm, ChangePass, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your  django views
def main_page(request):
    return render(request, "mainP.html", {})


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.error(request, 'You have been Logged In!')
            return redirect('/dashboard')

        else:
            messages.error(request, 'username or password not correct')

    return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST or None)
        # print(f.cleaned_data)
        if f.is_valid():
            obj = f.save(commit=False)
            obj.email = obj.username
            obj.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/login')
        else:
            print(f.is_valid())
            print(f.errors)
    else:
        f = SignUpForm()
    return render(request, 'registration.html', {'form': f})


@login_required
def dashboard_page(request):
    return render(request, 'dashboard.html', context=None)


@login_required
def user_list_page(request):
    template_name = "Users.html"
    a = get_user_model().objects.all()
    # q=UsrReg.objects.all()
    context = {"object_list": a}
    return render(request, template_name, context)


@login_required
def posts_page(request):
    a = UsrPost.objects.all()
    template_name = "post.html"
    return render(request, template_name, {'object_list': a})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(UsrPost, pk=pk)
    is_liked = False
    if post.likes.exists():
        if post.likes.filter(person=request.user).first() is not None:
               is_liked=True
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user.first_name+" "+request.user.last_name
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_details.html', {'post': post,'is_liked':is_liked,'form': form})


@login_required
def like_post(request,pk):
    post = get_object_or_404(UsrPost, pk=pk)
    is_liked = False
    print("123")
    if post.likes.exists():
        if post.likes.filter(person=request.user).first() is not None:
            print("345")
            obj=LikePost.objects.filter(person=request.user)
            obj.delete()
            is_liked=False
        else:
            obj = LikePost.objects.create(person=request.user, post=post)
            is_liked = True

    else:
            obj=LikePost.objects.create(person=request.user,post=post)
            print("567")
            is_liked=True
    print("890")
    return redirect('post_detail',pk=post.pk)



@login_required
def make_post(request):

    f = PostForm(request.POST or None)
    if f.is_valid():
        obj = f.save(commit=False)
        obj.user = request.user
        obj.save()

        f = PostForm()
        return redirect('/dashboard/posts/')

    return render(request, "makepost.html", {'form': f})


@login_required
def profile_details_page(request):
    if request.user.is_authenticated:
        obj = get_user_model().objects.get(username=request.user.username)
        template_name = "profile.html"
        context = {"object": obj}
    return render(request, template_name, context)


@login_required
def edit_profile_page(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST,request.FILES or None,instance=request.user)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/profile')
    else:
        form = ChangeForm(instance=request.user)
    return render(request, 'editProfile.html', {'form': form})


@login_required
def change_password_request(request):
    if request.method == 'POST':
        form = ChangePass(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChangePass(user=request.user)
    return render(request, 'change_p.html', {'form': form})


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(UsrPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user.first_name+" "+request.user.last_name
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def logout_page(request):
    logout(request)
    return redirect('/')