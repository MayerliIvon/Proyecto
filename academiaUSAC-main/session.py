import json

def iniciar_sesion(usuario_entry, contrasena_entry, update_error_message, main_view_instance):
    # Obtener datos del usuario y contraseña
    user = usuario_entry.get()
    contrasena = contrasena_entry.get()
    isUser = False
    isPass = False
  
    # Leer el archivo JSON que contiene la información de los usuarios
    with open('./users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if user in item:
                isUser = True
                if isUser and item[user]['password'] == contrasena:
                    isPass = True
                    main_view_instance.reset_incorrect_password_count()  # Reset the incorrect password count on successful login
                elif isUser:
                    main_view_instance.incorrect_password_count += 1  # Increment the incorrect password count



    if not isUser:
        update_error_message('Usuario no registrado')
    else:
        update_error_message('')  # Clear the error message or hide it
        if not isPass and main_view_instance.incorrect_password_count >= 3:
            #UserStatus(user, False)
            update_error_message('Usuario bloqueado')
        elif not isPass:
            update_error_message('Contraseña incorrecta')