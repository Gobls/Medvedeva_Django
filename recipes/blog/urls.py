from django.urls import path, re_path
from blog.views import *


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('cats/<slug:rec>', categories),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('registr/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:cat_slug>', PostCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    re_path(r'^archive/(?P<number>[0-9]{6})/', archive)
]
