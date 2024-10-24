# Create your models here.
from django.db import models
from django.core.validators import EmailValidator # permite validar el formato del correo (nombre@dominio.com), si es diferente genera un error de validación
from django.core.validators import MinValueValidator # permite validar la entrada de un numero minimo requerido, si no cumple el requisito genera un error de validación
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError # se genera cuando hay un error de validación, se utiliza para manejar errores que ocurren durante la validación de datos

# En este archivo van todos los modelos 
# modelo de GUEST
class Guest(models.Model):
    guest_name = models.CharField(max_length = 30, blank=False, null=False)
    guest_lastname = models.CharField(max_length = 30, blank=False, null=False)
    guest_age = models.IntegerField(
        validators=[MinValueValidator(18, message="La edad debe ser al menos 18 años")],
        blank=False, 
        null=False
        )
    guest_email = models.EmailField(
        validators=[EmailValidator(message="Por favor, introduce un correo electrónico válido")], 
        unique=True, 
        blank=False, 
        null=False
    )
    guest_phonenumber = models.IntegerField(blank=False, null=False)
    guest_created_at = models.DateTimeField(auto_now_add=True)
    guest_updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.guest_name} {self.guest_lastname}"
    
# modelo de ROOM
class Room(models.Model):
    room_number = models.IntegerField(
    validators=[MinValueValidator(1, message="El número de habitación debe ser un mayor a 1")],
    unique=True
    )
    room_type = models.CharField(max_length = 100)
    room_created_at = models.DateTimeField(auto_now_add=True)
    room_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.room_number 
    
# modelo de RESERVATION
class Reservation(models.Model):
    reservation_number = models.IntegerField()
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_id= models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in= models.DateField()
    check_out= models.DateField()
    reservation_created_at = models.DateTimeField(auto_now_add=True)
    reservation_updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.check_in >= self.check_out:
            raise ValidationError("La fecha de check-out debe ser posterior a la de check-in.")

    def __str__(self):
        return self.reservation_number
    
# modelo de REVIEW
class Reviews(models.Model):
    review_number = models.IntegerField(
        validators=[MinValueValidator(0, message="El número de review debe ser un número igual o mayor a 5"), 
        MaxLengthValidator(5, message="El número de review debe ser un número igual o menor a 5")],
        unique=True
    )
    review_comment = models.TextField(max_length=200)
    reservation_id= models.ForeignKey(Reservation, on_delete=models.CASCADE)
    review_created_at = models.DateTimeField(auto_now_add=True)
    review_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_number
