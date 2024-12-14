import requests
import mysql.connector
from datetime import datetime
import os
import time

# Función para conectarse a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecotech_db"
    )

# Función para buscar indicadores utilizando la API
def buscar_indicador(indicador):
    url = f"https://mindicador.cl/api/{indicador}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Si hay un error en la solicitud, lanza una excepción
        data = response.json()

        # Extraer la información relevante y limpiar los datos
        if 'serie' in data:
            # Obtener el valor más reciente de la serie de datos
            ultimo_indicador = data['serie'][0]
            fecha = ultimo_indicador['fecha']
            valor = ultimo_indicador['valor']
            return valor, fecha
        else:
            print(f"No se encontró información para el indicador {indicador}.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None, None

# Función para almacenar un indicador en la base de datos
def almacenar_en_bd(nombre, valor, fecha, fuente="Mindicador.cl"):
    db = conectar_bd()
    cursor = db.cursor()
    query = "INSERT INTO indicadores (nombre, valor, fecha_actualizacion, fuente) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, valor, fecha, fuente))
    db.commit()
    cursor.close()
    db.close()
    print(f"Indicador {nombre} almacenado exitosamente en la base de datos.")
    time.sleep(5)

# Menú principal
def menu():        
    while True:
        print("\n*** Consulta de Indicadores Económicos ***")
        print("1. Unidad de Fomento (UF)")
        print("2. Índice de Valor Promedio (IVP)")
        print("3. Índice de Precio al Consumidor (IPC)")
        print("4. Unidad Tributaria Mensual (UTM)")
        print("5. Dólar Observado")
        print("6. Euro")
        print("7. Ver datos almacenados")
        print("8. Salir")

        opcion = input("¿Qué indicador deseas buscar hoy? (1-8): ")
        indicadores = {
            '1': 'uf',
            '2': 'ivp',
            '3': 'ipc',
            '4': 'utm',
            '5': 'dolar',
            '6': 'euro'
        }

        if opcion == '8':
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        if opcion == '7':
            ver_datos_almacenados()
            continue

        if opcion in indicadores:
            indicador = indicadores[opcion]
            print(f"Buscando información sobre {indicador}...")
            valor, fecha_actualizacion = buscar_indicador(indicador)

            if valor is not None and fecha_actualizacion is not None:
                # Convertir la fecha a un formato más adecuado para la base de datos
                fecha_actualizacion = datetime.strptime(fecha_actualizacion, "%Y-%m-%dT%H:%M:%S.%fZ")
                print(f"Valor: {valor}, Fecha de Actualización: {fecha_actualizacion}")
                almacenar = input("¿Deseas almacenar este dato en la base de datos? (S/N): ").upper()
                if almacenar == 'S':
                    almacenar_en_bd(indicador, valor, fecha_actualizacion)
            else:
                print(f"No se pudo obtener información relevante sobre {indicador}.")
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 8.")

# Función para ver los datos almacenados en la base de datos
def ver_datos_almacenados():
    db = conectar_bd()
    cursor = db.cursor()
    query = "SELECT nombre, valor, fecha_actualizacion, fuente FROM indicadores"
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    print("\n*** Datos Almacenados en la Base de Datos ***")
    for fila in resultados:
        print(f"Indicador: {fila[0]}, Valor: {fila[1]}, Fecha de Actualización: {fila[2]}, Fuente: {fila[3]}")
    time.sleep(5)
    cursor.close()
    db.close()

# Iniciar el menú
menu()
