from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentCreateDeleteView, TagViewSet, LikedPostsView


router = DefaultRouter()
router.register('post', PostViewSet, 'post')
router.register('comment', CommentCreateDeleteView, 'comment')  # для обработки нескольких запросов 
router.register('tags', TagViewSet, 'tags')
urlpatterns = [
    path('liked/', LikedPostsView.as_view(), name='liked') # для обработки одного запроса 

]
urlpatterns += router.urls











