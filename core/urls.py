"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include the blog app's URLs
    
    # path('', views.index, name='index'),  # homepage
    # path('upload-story/', views.upload_story, name='upload_story'),
    # path('fiction/', views.fiction, name='fiction'),  # fiction category
    # path('truecrime/', views.truecrime, name='truecrime'),  # true crime category
    # path('my-corner/', views.my_corner, name='my_corner'),  # my corner page
    # path('story/<int:pk>/', views.story_detail, name='story_detail'),  # single story
    # path('category/<str:category>/', views.category_list, name='category_list'),  # generic category
    # path('choose-category/<int:story_id>/', views.choose_category, name='choose_category'),  # choose category step

]
