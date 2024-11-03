import mysql.connector
from colorama import Fore, Style

#Aqui hubiera estado la coneccion a la base de datos pero no pude darle temrino :C
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="ecotech_db"  
    )

# Función para registrar un nuevo empleado
def registrar_empleado():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Registrando un nuevo empleado..." + Style.RESET_ALL)
    nombre = input("Nombre del empleado: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Correo Electrónico: ")
    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    salario = float(input("Salario: "))

    query = "INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, direccion, telefono, email, fecha_inicio, salario))
    db.commit()
    cursor.close()
    db.close()
    print(Fore.GREEN + "Empleado registrado exitosamente." + Style.RESET_ALL)

# Función para gestionar departamentos
def gestionar_departamentos():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Gestionando departamentos..." + Style.RESET_ALL)
    opcion = input("¿Deseas (C)rear, (E)ditar, (B)uscar o (D)eletear un departamento? ").upper()

    if opcion == 'C':
        nombre_depto = input("Nombre del departamento: ")
        gerente = input("Gerente del departamento: ")
        query = "INSERT INTO departamentos (nombre, gerente) VALUES (%s, %s)"
        cursor.execute(query, (nombre_depto, gerente))
        db.commit()
        print(Fore.GREEN + "Departamento creado exitosamente." + Style.RESET_ALL)
    
    elif opcion == 'E':
        id_depto = int(input("ID del departamento a editar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        query = "UPDATE departamentos SET nombre = %s WHERE id = %s"
        cursor.execute(query, (nuevo_nombre, id_depto))
        db.commit()
        print(Fore.GREEN + "Departamento actualizado." + Style.RESET_ALL)

    elif opcion == 'B':
        nombre_buscar = input("Nombre del departamento a buscar: ")
        query = "SELECT * FROM departamentos WHERE nombre LIKE %s"
        cursor.execute(query, ('%' + nombre_buscar + '%',))
        resultados = cursor.fetchall()
        for depto in resultados:
            print(depto)

    elif opcion == 'D':
        id_depto = int(input("ID del departamento a eliminar: "))
        query = "DELETE FROM departamentos WHERE id = %s"
        cursor.execute(query, (id_depto,))
        db.commit()
        print(Fore.RED + "Departamento eliminado." + Style.RESET_ALL)

    cursor.close()
    db.close()

# Función para asignar un empleado a un departamento
def asignar_empleado_departamento():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Asignando empleado a un departamento..." + Style.RESET_ALL)
    id_empleado = int(input("ID del empleado: "))
    id_departamento = int(input("ID del departamento: "))
    query = "UPDATE empleados SET id_departamento = %s WHERE id = %s"
    cursor.execute(query, (id_departamento, id_empleado))
    db.commit()
    cursor.close()
    db.close()
    print(Fore.GREEN + "Empleado asignado al departamento exitosamente." + Style.RESET_ALL)

# Función para registrar tiempo trabajado
def registrar_tiempo():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Registrando tiempo trabajado..." + Style.RESET_ALL)
    id_empleado = int(input("ID del empleado: "))
    id_proyecto = int(input("ID del proyecto: "))
    fecha = input("Fecha (AAAA-MM-DD): ")
    horas = float(input("Horas trabajadas: "))
    descripcion = input("Descripción de tareas realizadas: ")

    query = "INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, horas, descripcion) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id_empleado, id_proyecto, fecha, horas, descripcion))
    db.commit()
    cursor.close()
    db.close()
    print(Fore.GREEN + "Tiempo registrado exitosamente." + Style.RESET_ALL)

# Función para gestionar proyectos
def gestionar_proyectos():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Gestionando proyectos..." + Style.RESET_ALL)
    opcion = input("¿Deseas (C)rear, (E)ditar o (D)eletear un proyecto? ").upper()

    if opcion == 'C':
        nombre_proyecto = input("Nombre del proyecto: ")
        descripcion = input("Descripción del proyecto: ")
        fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
        query = "INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre_proyecto, descripcion, fecha_inicio))
        db.commit()
        print(Fore.GREEN + "Proyecto creado exitosamente." + Style.RESET_ALL)

    elif opcion == 'E':
        id_proyecto = int(input("ID del proyecto a editar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        query = "UPDATE proyectos SET nombre = %s WHERE id = %s"
        cursor.execute(query, (nuevo_nombre, id_proyecto))
        db.commit()
        print(Fore.GREEN + "Proyecto actualizado." + Style.RESET_ALL)

    elif opcion == 'D':
        id_proyecto = int(input("ID del proyecto a eliminar: "))
        query = "DELETE FROM proyectos WHERE id = %s"
        cursor.execute(query, (id_proyecto,))
        db.commit()
        print(Fore.RED + "Proyecto eliminado." + Style.RESET_ALL)

    cursor.close()
    db.close()

# Función para asignar un empleado a un proyecto
def asignar_empleado_proyecto():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Asignando empleado a un proyecto..." + Style.RESET_ALL)
    id_empleado = int(input("ID del empleado: "))
    id_proyecto = int(input("ID del proyecto: "))
    query = "INSERT INTO asignaciones (id_empleado, id_proyecto) VALUES (%s, %s)"
    cursor.execute(query, (id_empleado, id_proyecto))
    db.commit()
    cursor.close()
    db.close()
    print(Fore.GREEN + "Empleado asignado al proyecto exitosamente." + Style.RESET_ALL)

# Función para generar informes
def generar_informes():
    db = conectar_bd()
    cursor = db.cursor()
    print(Fore.GREEN + "Generando informes..." + Style.RESET_ALL)
    # Lógica para obtener datos de la base y exportar a PDF o Excel
    # (puedes utilizar bibliotecas como pandas o reportlab aquí)
    cursor.close()
    db.close()
    print(Fore.GREEN + "Informe generado." + Style.RESET_ALL)


# Menú principal interactivo con colores
def menu():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "\n*** Sistema de Gestión de Empleados de EcoTech Solutions ***" + Style.RESET_ALL)
        print("1. Registrar nuevo empleado")
        print("2. Gestión de departamentos")
        print("3. Asignación de empleados a departamentos")
        print("4. Registro de tiempo")
        print("5. Gestión de proyectos")
        print("6. Asignación de empleados a proyectos")
        print("7. Generar informes")
        print("8. Salir")
        
        opcion = input(Fore.CYAN + "Selecciona una opción: " + Style.RESET_ALL)
        
        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            gestionar_departamentos()
        elif opcion == '3':
            asignar_empleado_departamento()
        elif opcion == '4':
            registrar_tiempo()
        elif opcion == '5':
            gestionar_proyectos()
        elif opcion == '6':
            asignar_empleado_proyecto()
        elif opcion == '7':
            generar_informes()
        elif opcion == '8':
            print(Fore.RED + "Saliendo del sistema... ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + "Opción no válida. Inténtalo de nuevo." + Style.RESET_ALL)

menu()
