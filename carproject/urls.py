from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import CarViewSet
from carmodelapp.views import CarViewSet ,OwnerViewSet



router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'owners', OwnerViewSet, basename='Owner')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

