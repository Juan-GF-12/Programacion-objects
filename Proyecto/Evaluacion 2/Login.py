import requests
import bcrypt

BASE_URL = "https://jsonplaceholder.typicode.com/users"

# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    salt = bcrypt.gensalt()  # Generamos una sal para encriptar
    return bcrypt.hashpw(contraseña.encode('utf-8'), salt)

# Función para verificar la contraseña encriptada
def verificar_contraseña(contraseña, contraseña_encriptada):
    return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada)

# Crear un nuevo usuario
def crear_usuario(nombre, correo, contraseña):
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Encriptar la contraseña
    contraseña_encriptada = encriptar_contraseña(contraseña)

    # Datos del nuevo usuario
    nuevo_usuario = {
        "name": nombre,
        "email": correo,
        "password": contraseña_encriptada.decode('utf-8')  # Convercion de la contraseña a texto
    }
    
    # solicitud post
    response = requests.post(url, json=nuevo_usuario)

    # Verificamos si la creación fue exitosa
    if response.status_code == 201:
        print(f"Usuario creado con éxito: {nuevo_usuario['name']}")
    else:
        print(f"Error al crear usuario: {response.status_code}")
        print(response.json())

# Actualizar un usuario
def actualizar_usuario(id_usuario, nombre=None, correo=None, contraseña=None):
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    
    # Datos a actualizar (no se actualizaran todos los campos si no se proporcionan)
    datos_actualizados = {}
    if nombre:
        datos_actualizados["name"] = nombre
    if correo:
        datos_actualizados["email"] = correo
    if contraseña:
        datos_actualizados["password"] = encriptar_contraseña(contraseña).decode('utf-8')  # Encriptamos la nueva contraseña

    # solicitud PUT
    response = requests.put(url, json=datos_actualizados)

    # Verificamos si la actualización fue exitosa
    if response.status_code == 200:
        print(f"Usuario editado con éxito: {datos_actualizados}")
    else:
        print(f"Error al editar usuario: {response.status_code}")
        print(response.json())

# Eliminar un usuario
def eliminar_usuario(id_usuario):
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    
    # solicitud DELETE
    response = requests.delete(url)

    # Verificamos si la eliminación fue exitosa
    if response.status_code == 200:
        print(f"Usuario con ID {id_usuario} eliminado con éxito.")
    else:
        print(f"Error al eliminar usuario: {response.status_code}")
        print(response.json())

# Autenticación de usuario
def autenticar_usuario(correo, contraseña):
    url = "https://jsonplaceholder.typicode.com/users"
    
    # solicitud GET para obtener todos los usuarios
    response = requests.get(url)
    
    if response.status_code == 200:
        usuarios = response.json()
        
        # Buscamos el usuario por correo
        for usuario in usuarios:
            if usuario["email"] == correo:
                # Verificamos la contraseña
                contraseña_encriptada = usuario.get("password", "")
                if verificar_contraseña(contraseña, contraseña_encriptada.encode('utf-8')):
                    print(f"Autenticación exitosa para {usuario['name']}")
                    return True
                else:
                    print("Contraseña incorrecta.")
                    return False
        print("Usuario no encontrado.")
        return False
    else:
        print(f"Error al autenticar: {response.status_code}")
        return False

# Menú interactivo
def menu():
    while True:
        print("\n*** Menú de Opciones ***")
        print("1. Crear un usuario")
        print("2. Actualizar un usuario")
        print("3. Eliminar un usuario")
        print("4. Autenticar usuario")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo del usuario: ")
            contraseña = input("Ingrese la contraseña del usuario (La contraseña debe tener al menos 8 caracteres): ")
            crear_usuario(nombre, correo, contraseña)
        elif opcion == '2':
            id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
            nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea cambiarlo): ")
            correo = input("Ingrese el nuevo correo (deje en blanco si no desea cambiarlo): ")
            contraseña = input("Ingrese la nueva contraseña (deje en blanco si no desea cambiarla): ")
            actualizar_usuario(id_usuario, nombre, correo, contraseña)
        elif opcion == '3':
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
        elif opcion == '4':
            correo = input("Ingrese el correo del usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            autenticar_usuario(correo, contraseña)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

# Ejecutar el menú
menu()
