# Create your views here.
from rest_framework import generics
from .models import Guest
from .models import Room
from .models import Reservation
from .models import Reviews
from .serializers import GuestSerializer
from .serializers import RoomSerializer
from .serializers import ReservationSerializer
from .serializers import ReviewsSerializer
from rest_framework.permissions import IsAuthenticated

#Metodos para Guest
class GuestListCreate(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

#Metodos para Room 
class RoomListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#Metodos para Reservation
class ReservationListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#Metodos para Reviews
class ReviewsListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer