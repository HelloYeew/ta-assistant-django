from django.urls import path
from . import views
from .views import ClassCreateView

urlpatterns = [
    path('', views.home, name='classroom-home'),
    path('new-class/', ClassCreateView.as_view(), name='new-class')
]