from django.urls import path

from . import views

urlpatterns = [
    path('categories/', view=views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>', view=views.CategoryListCreateAPIView.as_view())
]