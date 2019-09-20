from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    # path('skills/', views.skills_index, name='index'),
    path('wishs/create/', views.WishCreate.as_view(), name='wishs_create'),
    path('wishs/<int:pk>/delete/', views.WishDelete.as_view(), name='wishs_delete'),
]