# Clase para generar informes de empleados, proyectos y departamentos
class Informe:
    def __init__(self):
        self.datos = []

    def agregar_datos(self, informacion):
        self.datos.append(informacion)

    def exportar_pdf(self):
        # Implementación para exportar en PDF
        print("Exportando datos en formato PDF...")
    
    def exportar_excel(self):
        # Implementación para exportar en Excel
        print("Exportando datos en formato Excel...")
