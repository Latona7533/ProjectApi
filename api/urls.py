from django.urls import path, include
from .viewsets import PostsApiView, PostApiView, AllPostsApiList, PostsApiDetail, PstViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PstViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #базовый развернутый способ при помощи Api View
    path('posts/', PostsApiView.as_view()),
    path('post/<int:pk>', PostApiView.as_view()),
    # второй способ с дженериками по проще
    path('psts/', AllPostsApiList.as_view()),
    path('psts/<int:pk>', PostsApiDetail.as_view()),
    #третий способ с ModelViewSet и неявный


    path('postsview/', PstViewSet.as_view({'get': 'list'})),
    path('postsview/<int:pk>', PstViewSet.as_view({'put': 'update'})),

]