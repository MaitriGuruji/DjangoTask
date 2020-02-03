from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import user_list_page,profile_details_page,posts_page,make_post,post_detail,add_comment_to_post,like_post

urlpatterns = [
    path('users/',user_list_page),
    # path('like/',like_post, name='like_post'),
    path('posts/<int:pk>/like/',like_post,name='like_post'),
    path('posts/',posts_page),
    path('posts/<int:pk>/',post_detail, name='post_detail'),
    path('addpost/',make_post),
    path('profile/',profile_details_page),
    path('posts/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
]

# if settings.DEBUG:
#
#     # from django.conf.urls.static import static
#     urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
