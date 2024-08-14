from django.urls import include, path
from rest_framework.authtoken import views


# import routers
from rest_framework import routers 
# import everything from views
from api.views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/',views .obtain_auth_token)
    # path('app-auth/', include('rest_framework.urls', namespace='rest_framework')) # this line is used for only login & logout feature in DRF window
]