from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.home_page),
    path('post/<int:post_id>', blog.views.post_page),
]
