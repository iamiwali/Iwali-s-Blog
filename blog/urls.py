# blog/urls.py
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mycorner/', views.my_corner, name='my_corner'),
    path('fiction/', views.fiction, name='fiction'),
    path('truecrime/', views.truecrime, name='truecrime'),

    path('upload/', views.upload_story, name='upload_story'),
    path('choose-category/<int:story_id>/', views.choose_category, name='choose_category'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
    path('stories/', views.story_list, name='story_list'),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"), 

     # Password Reset (Recovery Email)
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # Dynamic category listing
    re_path(r'^(?!favicon\.ico$)(?P<category>[\w-]+)/$', views.category_list, name='category_list'),
    path('delete-story/<int:story_id>/', views.delete_story, name='delete_story'),
]
