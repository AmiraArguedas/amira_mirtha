from django.urls import path
from . import views

urlpatterns = [
    path('guests/', views.GuestListCreate.as_view(), name='guest-list'),
    path('guests/<int:pk>/', views.GuestDetail.as_view(), name='guest-detail'),
    path('rooms/', views.RoomListCreate.as_view(), name='producto-list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='producto-detail'),
    path('reservations/', views.ReservationListCreate.as_view(), name='producto-list'),
    path('reservations/<int:pk>/', views.ReservationDetail.as_view(), name='producto-detail'),
    path('reviews/', views.ReviewsListCreate.as_view(), name='producto-list'),
    path('reviews/<int:pk>/', views.ReviewsDetail.as_view(), name='producto-detail'),
]
