class Prestamo:
    def __init__(self, libro, usuario, fecha_inicio, fecha_fin):
        self.libro = libro  # Libro object
        self.usuario = usuario  # Usuario object
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
