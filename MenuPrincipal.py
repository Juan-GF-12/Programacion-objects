from Autor import Autor
from DetalleLibro import DetalleLibro
from Editorial import Editorial
from Categoria import Categoria
from Libro import Libro
from Usuario import Usuario
from TipoUsuario import TipoUsuario
from Prestamo import Prestamo
from Biblioteca import Biblioteca

# Crear la biblioteca
biblioteca = Biblioteca("Biblioteca Central")

def mostrar_menu():
    print("\nMenú Biblioteca")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Registrar préstamo")
    print("4. Ver libros")
    print("5. Ver usuarios")
    print("6. Ver préstamos")
    print("7. Salir")

def agregar_libro():
    titulo = input("Título del libro: ")
    autor_nombre = input("Nombre del autor: ")
    nacionalidad = input("Nacionalidad del autor: ")
    autor = Autor(autor_nombre, nacionalidad)
    
    editorial_nombre = input("Nombre de la editorial: ")
    editorial = Editorial(editorial_nombre)

    categoria_nombre = input("Nombre de la categoría: ")
    categoria = Categoria(categoria_nombre)

    fecha_lanzamiento = input("Fecha de lanzamiento: ")
    pais = input("País: ")
    total_hojas = int(input("Total de hojas: "))
    detalle_libro = DetalleLibro(fecha_lanzamiento, pais, total_hojas)

    libro = Libro(titulo, autor, editorial, categoria, detalle_libro)
    biblioteca.agregar_libro(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def agregar_usuario():
    nombre = input("Nombre del usuario: ")
    print("Tipo de usuario: 1. Usuario, 2. Administrador")
    tipo_opcion = input("Selecciona el tipo de usuario (1 o 2): ")

    if tipo_opcion == "1":
        tipo = "usuario"
    elif tipo_opcion == "2":
        tipo = "administrador"
    else:
        print("Opción no válida, por defecto será 'usuario'.")
        tipo = "usuario"

    tipo_usuario = TipoUsuario(tipo)
    usuario = Usuario(nombre, tipo_usuario)
    biblioteca.agregar_usuario(usuario)
    print(f"Usuario '{nombre}' con tipo '{tipo}' agregado exitosamente.")

def registrar_prestamo():
    libro_titulo = input("Título del libro a prestar: ")
    libro = next((l for l in biblioteca.libros if l.titulo == libro_titulo), None)

    if not libro:
        print(f"Libro '{libro_titulo}' no encontrado.")
        return

    usuario_nombre = input("Nombre del usuario que pide el préstamo: ")
    usuario = next((u for u in biblioteca.usuarios if u.nombre == usuario_nombre), None)

    if not usuario:
        print(f"Usuario '{usuario_nombre}' no encontrado.")
        return

    fecha_inicio = input("Fecha de inicio del préstamo: ")
    fecha_fin = input("Fecha de fin del préstamo: ")
    prestamo = Prestamo(libro, usuario, fecha_inicio, fecha_fin)
    biblioteca.registrar_prestamo(prestamo)
    print(f"Préstamo registrado exitosamente.")

def ver_libros():
    if biblioteca.libros:
        print("\nLista de libros:")
        for libro in biblioteca.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor.nombre}, Editorial: {libro.editorial.nombre}")
    else:
        print("No hay libros registrados.")

def ver_usuarios():
    if biblioteca.usuarios:
        print("\nLista de usuarios:")
        for usuario in biblioteca.usuarios:
            print(f"Nombre: {usuario.nombre}, Tipo: {usuario.tipo_usuario.tipo}")
    else:
        print("No hay usuarios registrados.")

def ver_prestamos():
    if biblioteca.prestamos:
        print("\nLista de préstamos:")
        for prestamo in biblioteca.prestamos:
            print(f"Libro: {prestamo.libro.titulo}, Usuario: {prestamo.usuario.nombre}, Fecha Inicio: {prestamo.fecha_inicio}, Fecha Fin: {prestamo.fecha_fin}")
    else:
        print("No hay préstamos registrados.")

# Menú interactivo
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        agregar_usuario()
    elif opcion == "3":
        registrar_prestamo()
    elif opcion == "4":
        ver_libros()
    elif opcion == "5":
        ver_usuarios()
    elif opcion == "6":
        ver_prestamos()
    elif opcion == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
