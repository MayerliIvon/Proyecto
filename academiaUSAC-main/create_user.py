import json

# Function to create a user dictionary
def CreateAlumnDict(username, nombre, apellido, fecha_nacimiento, telefono, dpi, email, password):
    return {
        username: {
            "nombre": nombre,
            "apellido": apellido,
            "fecha": fecha_nacimiento,
            "telf": telefono,
            "dpi": dpi,
            "email": email,
            "password": password, #if change, change on inicar_sesion()
            "tipo": "alumn",
            "confirm": "false" #la cuenta se crea pero esta bloqueada por defecto
        }
    }

def CreateCatdrDict(username, nombre, apellido, dpi, password):
    return {
        username: {
            "nombre": nombre,
            "apellido": apellido,
            "fecha": "-",
            "telf": "-",
            "dpi": dpi,
            "email": "-",
            "password": password, #if change, change on inicar_sesion()
            "tipo": "cat",
            "confirm": "false" #la cuenta se crea pero esta bloqueada por defecto
        }
    }

def JSONBuilder(usuario):
    # Read existing data
    with open('users.json', 'r') as f:
        try:
            users_list = json.load(f)
        except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
            users_list = []

    # Append new user data
    users_list.append(usuario)  # changed from user1 to user

    # Write the updated data back to the file
    with open('users.json', 'w') as f:
        json.dump(users_list, f, indent=4)