from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('directories', views.DirectoryViewSet)
router.register('directory_items', views.DirectoryItemsViewSet)
urlpatterns = [
    path(r'directory_items/<int:id>', views.ItemsByDirectories.as_view({'get': 'list'})),
    path(r'directories/<date>', views.DirectoriesByTime.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
