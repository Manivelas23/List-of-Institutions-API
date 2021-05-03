from django.contrib import admin
from django.urls import path,include
from .views import institutionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('institutions',institutionViewSet,basename='institutions')

urlpatterns = [
    path('institutions/', include(router.urls)),
    path('institutions/<int:pk>/',include(router.urls))
]
