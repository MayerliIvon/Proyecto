#import os
import json

nombres = ''
apellidos = ''
dpi = ''
fecha_nacimiento = ''
avatar = ''
usuario = ''
contrasena = ''
email = ''
phone = ''
user_type = ''

def CreateUser(nombres, apellidos, dpi, fecha_nacimiento, avatar, usuario, contrasena, email, phone, user_type):
    # Read existing data
    with open('users.json', 'r') as f:
        try:
            users_list = json.load(f)
        except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
            users_list = []
    
    # Append new user data
    users_list.append({
        usuario: {
            "nombres": nombres,
            "apellidos": apellidos,
            "dpi": dpi,
            "nacimiento": fecha_nacimiento,
            "avatar": avatar,
            "password": contrasena,
            "email": email,
            "phone": phone,
            "tipo": user_type,
            "confirm": "false"  # la cuenta se crea pero esta bloqueada por defecto
        }
    })
    
    # Write the updated data back to the file
    with open('users.json', 'w') as f:
        json.dump(users_list, f, indent=4)

# Update user status
def UserStatus(user):
    # Open the file to read
    with open('users.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)

    # Iterate through the list of dictionaries
    for item in data:
        # Check if the dictionary has the key 'admin'
        if user in item:
            if not status:
                item[user]['confirm'] = False
            else:
                item[user]['confirm'] = True
            

    # Convert the updated data back to a JSON string
    newData = json.dumps(data, indent=4)

    # Open the file to write
    with open('users.json', 'w') as file:
        # Write the updated JSON data to the file
        file.write(newData)