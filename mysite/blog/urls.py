from blog.views import *
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category')
]