from django.urls import path
from . import views


app_name = 'videos'

urlpatterns = [
    path('', views.videos_list, name='list'),
    path('rgister/', views.videos_test, name='test'),
    path('new-video/', views.video_new, name='new-video'),
    path('<slug:slug>', views.video_page, name='page'),
    path('search/', views.search_videos, name='search'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('settings/', views.settings_page, name='settings'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('video/<slug:slug>/like/', views.like_video, name='like'),
    path('video/<slug:slug>/dislike/', views.dislike_video, name='dislike'),
    
]