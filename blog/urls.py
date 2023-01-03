from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryView, BlogView

router = DefaultRouter()
router.register("category", CategoryView)
router.register("blog", BlogView)

urlpatterns = [
    path("", include(router.urls))
]