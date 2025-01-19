from django.urls import path
from dj_rest_auth.views import LoginView

from . import views

urlpatterns = [
    path('categories/', view=views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>', view=views.CategoryListCreateAPIView.as_view()),
    path('login', LoginView.as_view(), name='login')
]