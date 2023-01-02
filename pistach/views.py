from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from .forms import SignInForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pistach/index.html')

class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'pistach/posts.html', context={
            'posts': posts
        })
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'pistach/posts.html', context={
            'posts': posts
        })

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'pistach/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'pistach/signup.html', context={
            'form': form,
        })

class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'pistach/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'pistach/signin.html', context={
            'form': form,
        })

class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'pistach/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['catschoolwitcher82@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'pistach/contact.html', context={
            'form': form,
        })
class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pistach/success.html', context={
            'title': 'Спасибо'
        })
class VideosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pistach/videos.html')

