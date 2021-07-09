from django.urls import path
from . import views
from .views import ClassCreateView, ClassDetailView, ClassUpdateMember, ClassDeleteView

urlpatterns = [
    path('', views.home, name='classroom-home'),
    path('new-class/', ClassCreateView.as_view(), name='new-class'),
    path('class/<int:pk>', ClassDetailView.as_view(), name="class-detail"),
    path('class/<int:pk>/edit-member', ClassUpdateMember.as_view(), name="class-edit-member"),
    path('class/<int:pk>/member', views.view_member, name="class-member"),
    path('class/<int:pk>/delete', ClassDeleteView.as_view(), name="class-delete")
]