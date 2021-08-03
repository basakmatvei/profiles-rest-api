from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('directory_items', views.directory_items, name='directory_items'),
    path('by_directory_items/<int:id>/', views.by_directory_items,name='by_directory_items/<int:id>'),
    path('by_directory_items', views.by_directory_items_basic, name='by_directory_items_basic'),
    path('directories_bydate', views.directories_bydate_basic, name='directories_bydate_basic'),
    path('directories_bydate/?start_date=<str:start_date>', views.directories_bydate)
]
