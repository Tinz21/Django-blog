from email.mime import base
from rest_framework.routers import DefaultRouter
from comments.api.views import CommentViewSet


router_comment = DefaultRouter()
router_comment.register(prefix='comments', viewset=CommentViewSet, basename='comment')
