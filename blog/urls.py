from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from . import views
from django.urls import path

from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path('', views.post_list, name='home'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post_like/<int:post_id>', views.post_like, name='post_like')
]
