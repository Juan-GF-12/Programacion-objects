#Clase para crear a empleado
class Empleado:
    def __init__(self, nombre, direccion, telefono, email, fecha_inicio, salario):
        self.id_empleado = None  # ID único asignado automáticamente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario