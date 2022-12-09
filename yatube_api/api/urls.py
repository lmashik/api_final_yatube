from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (
	PostViewSet,
	GroupViewSet,
	CommentViewSet,
	FollowViewSet
)

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='followings')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('auth/', include('djoser.urls.jwt'))
]
