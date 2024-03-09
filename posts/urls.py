from django.urls import path
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

# PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
# urlpatterns = [
# path('lists/', PostList.as_view()),
# path('<int:pk>/', PostDetail.as_view()),
# path('users/', UserList.as_view()),
# path('users/<int:pk>/', UserDetail.as_view()),

# ]
