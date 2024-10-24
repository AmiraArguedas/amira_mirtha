# Proyecto realizado por Amira y Mirtha
#Autenticaión mediante Simple JWT de Django.
Ruta de acceso libre:
http://localhost:8000/api/guests/

Las rutas protegidas son:
http://localhost:8000/api/rooms/
http://localhost:8000/api/reservations/
http://localhost:8000/api/reviews/

Para poder consultar a los endpoints protegidos:
http://127.0.0.1:8000/api/token/ 
# Hacemos un post y en body se envian los datos de ingreso para obtener el access del super-usuario y poder acceder a la ruta protegida con el JWT

{
    "username": "...",
    "password": "..."
}

# Vamos a obtener una respuesta que contiene el token de acceso y este lo debemos enviar (en Authorization) cada vez que hagamos una consulta a los endpoints protegidos 
#Realizacion de consultas a los endpoints

##################Endpoint Guest#################################
# Get
http://localhost:8000/api/guests/

# Post  
http://localhost:8000/api/guests/

En el body debemos enviar los siguientes datos en formato Json 
{
    "guest_name": "Juan",
    "guest_lastname": "Pérez",
    "guest_age": 25,
    "guest_email": "juan.perez@example.com",
    "guest_phonenumber": 123456789
}

# update 
http://localhost:8000/api/guests/1   # Debemos especificar el id 

En el body debemos enviar los siguientes datos en formato Json 
{
    "guest_name": "Juan",
    "guest_lastname": "Lopez",
    "guest_age": 28,
    "guest_email": "juan.lopez@example.com",
    "guest_phonenumber": 123455789
}

# delete 
http://localhost:8000/api/guests/1   # Debemos especificar el id 



##################Endpoint Guest#################################
# Get
http://localhost:8000/api/rooms/

# Post  
http://localhost:8000/api/rooms/

En el body debemos enviar los siguientes datos en formato Json 
{
    "room_number": 101,
    "room_type": "Doble"
}

# update 
http://localhost:8000/api/rooms/1   # Debemos especificar el id 

En el body debemos enviar los siguientes datos en formato Json 
{
    "room_number": 101,
    "room_type": "Single Room"
}

# delete 
http://localhost:8000/api/rooms/1   # Debemos especificar el id 




##################Endpoint Reservation#################################
# Get
http://localhost:8000/api/reservations/

# Post  
http://localhost:8000/api/reservations/

En el body debemos enviar los siguientes datos en formato Json 
{
    "reservation_number": // este numero esta formado por 6 digitos,
    "guest_id": 1,  // Asegúrate de que este ID corresponda a un huésped existente
    "room_id": 1,   // Asegúrate de que este ID corresponda a una habitación existente
    "check_in": "2024-10-01",
    "check_out": "2024-10-05"
}

# update 
http://localhost:8000/api/reservations/1   # Debemos especificar el id 

En el body debemos enviar los siguientes datos en formato Json 
{
    "reservation_number": // este numero esta formado por 6 digitos,
    "guest_id": 2,  // Asegúrate de que este ID corresponda a un huésped existente
    "room_id": 1,   // Asegúrate de que este ID corresponda a una habitación existente
    "check_in": "2024-11-01",
    "check_out": "2024-11-10"
}

# delete 
http://localhost:8000/api/reservations/1   # Debemos especificar el id 




##################Endpoint Review#################################
# Get
http://localhost:8000/api/reviews/

# Post  
http://localhost:8000/api/reviews/

En el body debemos enviar los siguientes datos en formato Json 

{
    "review_number": 5,  // Debe ser un número entre 0 y 5
    "review_comment": "Excelente servicio y muy buena experiencia.",
    "reservation_id": 1  // Asegúrate de que este ID corresponda a una reserva existente
}

# update 
http://localhost:8000/api/reviews/1   # Debemos especificar el id 

En el body debemos enviar los siguientes datos en formato Json 

{
    "review_number": 1,  // Debe ser un número entre 0 y 5
    "review_comment": "El lugar estaba sucio y desordenado.",
    "reservation_id": 1  // Asegúrate de que este ID corresponda a una reserva existente
}

# delete 
http://localhost:8000/api/reviews/1   # Debemos especificar el id 