import http.client
import json
import mysql.connector
from datetime import datetime

# Función para conectarse a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecotech_db"
    )

# Función para buscar indicadores utilizando la API
def buscar_indicador(nombre_indicador):
    conn = http.client.HTTPSConnection("google.serper.dev")
    info_busqueda = json.dumps({"q": nombre_indicador})
    headers = {
        'X-API-KEY': '4f044cd471e12a1204ee4d3e06e7b6f12bf57d40',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", info_busqueda, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return json.loads(data)

# Función para extraer la información relevante de la respuesta de la API
def extraer_informacion_api(respuesta_api):
    try:
        # Convertir la respuesta en formato JSON
        datos = json.loads(respuesta_api)
        
        # Verificar si hay un "answerBox" con una respuesta
        if "answerBox" in datos and "answer" in datos["answerBox"]:
            return datos["answerBox"]["answer"]
        
        # Si no se encuentra en answerBox, revisar los snippets
        for resultado in datos.get("organic", []):
            snippet = resultado.get("snippet", "")
            if "UF" in snippet:  # Búsqueda básica de "UF" en el texto
                return snippet
        
        # Si no hay resultados relevantes
        return "No se encontró información relevante."
    
    except Exception as e:
        return f"Error al procesar los datos: {e}"

# Función para procesar los resultados y extraer valor y fecha de actualización
def procesar_resultados(datos, indicador):
    try:
        # Verificar si hay un "answerBox" con una respuesta
        if "answerBox" in datos and "answer" in datos["answerBox"]:
            respuesta = datos["answerBox"]["answer"]
            valor = respuesta.split(" = ")[0]  # Obtener el valor antes del signo "="
            # Asumimos que la fecha de actualización puede ser extraída del contexto (aunque no está explícita en este caso)
            fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return valor, fecha_actualizacion
        
        # Si no se encuentra en answerBox, revisar los snippets
        for resultado in datos.get("organic", []):
            snippet = resultado.get("snippet", "")
            if "UF" in snippet:  # Búsqueda básica de "UF" en el texto
                valor = snippet.split(" = ")[0]  # Obtener el valor antes del signo "="
                fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return valor, fecha_actualizacion
        
        return None, None
    
    except Exception as e:
        print(f"Error al procesar los resultados: {e}")
        return None, None

# Función para almacenar un indicador en la base de datos
def almacenar_en_bd(nombre, valor, fecha, fuente="Google API"):
    db = conectar_bd()
    cursor = db.cursor()
    query = "INSERT INTO indicadores (nombre, valor, fecha_actualizacion, fuente) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, valor, fecha, fuente))
    db.commit()
    cursor.close()
    db.close()
    print(f"Indicador {nombre} almacenado exitosamente en la base de datos.")

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
        print("7. Salir")
        
        opcion = input("¿Qué indicador deseas buscar hoy? (1-7): ")
        indicadores = {
            '1': 'Unidad de Fomento',
            '2': 'Índice de Valor Promedio',
            '3': 'Índice de Precio al Consumidor',
            '4': 'Unidad Tributaria Mensual',
            '5': 'Dólar Observado',
            '6': 'Euro'
        }
        
        if opcion == '7':
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        
        if opcion in indicadores:
            indicador = indicadores[opcion]
            print(f"Buscando información sobre {indicador}...")
            datos = buscar_indicador(indicador)
            valor, fecha_actualizacion = procesar_resultados(datos, indicador)
            
            if valor is not None and fecha_actualizacion is not None:
                print(f"Valor: {valor}, Fecha de Actualización: {fecha_actualizacion}")
                almacenar = input("¿Deseas almacenar este dato en la base de datos? (S/N): ").upper()
                if almacenar == 'S':
                    almacenar_en_bd(indicador, valor, fecha_actualizacion)
            else:
                print(f"No se pudo obtener información relevante sobre {indicador}.")
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 7.")
menu()
