"""
URL configuration for gr48 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from posts.views import (main_view,
                         posts_list_view,
                         posts_detail_view,
                         post_create_view,
                         posts_detail_view,
                         post_update_view,
                         TestView,
                         PostListView)

from user.views import (register_view,
                        login_view,
                        logout_view,
                        profile_view)
from django.conf.urls.static import static
urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path("", main_view, name="main_view" ),
    path('posts/', posts_list_view),
    path('posts/<int:post_id>/', posts_detail_view),
    path('posts/create/', post_create_view),
    path("register/", register_view),
    path("login/", login_view),
    path("logout/",logout_view, name='logout'),
    path("profile/", profile_view),
    path("posts/update/<int:post_id>/", post_update_view),
    path("/test/", TestView.as_view()),
    path("/posts/class", PostListView.as_view())

    ]
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)