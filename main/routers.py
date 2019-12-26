from rest_framework import routers

from restapp.apiviews import PersonViewSet

router = routers.DefaultRouter()

router.register('person' , PersonViewSet , basename='person')


urlpatterns = router.urls

