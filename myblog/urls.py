from django.contrib import admin
from django.urls import path
from blog.views import PostListCreate

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('admin/', admin.site.urls),
]
