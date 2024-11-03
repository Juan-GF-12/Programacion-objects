# Clase para generar proyectos
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.id_proyecto = None  # ID único
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio