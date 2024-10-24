from rest_framework import serializers
from .models import Guest
from .models import Room
from .models import Reservation
from .models import Reviews


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        
    def validate_guest_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del huésped debe ser mayor a 2 letras")
        return value 
    
    def validate_guest_lastname(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("El nombre del huésped debe ser mayor a 2 letras")
        return value 
    
    def validate_guest_lastname(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("El nombre del huésped debe ser mayor a 2 letras")
        return value 
    

    def validate_email(self, value):
         if '@' not in value:
             raise serializers.ValidationError("El correo electrónico debe contener el símbolo '@'")
         return value
    
    def validate_guest_phonenumber(self, value):
        if value < 8:  
            raise serializers.ValidationError("El número de teléfono del huésped debe ser igual o mayor a 8 dígitos")
        return value



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
    def validate_room_type(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("El tipo de habitación tiene que contener más de 5 letras")
        return value 
    
    def validate_room_number(self,value):
        if value < 1:
            raise serializers.ValidationError("El número de la habitación debe ser igual o mayor a 1")
        return value 
        

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
    def valid_reservation_number(self, value):
        if value < 6 :
            raise serializers.ValidationError("El número de reservation debe contener al menos 6 dígitos.")
        return value 
    
    def valid_check_out_check_in(self, check_in, check_out, value):
        
        if check_in >= check_out:
            raise serializers.ValidationError("La fecha de check-out debe ser posterior a la de check-in.")
        return value 

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

def valid_review_number(self, value):
        if value >=0 and value <= 5 :
            raise serializers.ValidationError("La calificacion va desde 0-5")
        return value 

def valid_review_comment(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError("El campo de review no puede estar vacío.")
        return value