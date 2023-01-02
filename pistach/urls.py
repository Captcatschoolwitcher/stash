from django.contrib import admin
from django.urls import path
from .views import MainView, PostView, SignUpView, SignInView, FeedBackView, SuccessView, VideosView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('posts', PostView.as_view(), name='dashboard'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('videos/', VideosView.as_view(), name='videos'),
]
