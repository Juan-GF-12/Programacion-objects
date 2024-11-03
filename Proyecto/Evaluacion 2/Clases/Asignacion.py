# Clase para asignar a los empleados a departamentos y proyectos
class Asignacion:
    def __init__(self, empleado, departamento=None, proyecto=None):
        self.empleado = empleado
        self.departamento = departamento
        self.proyecto = proyecto

    def asignar_departamento(self, departamento):
        self.departamento = departamento

    def asignar_proyecto(self, proyecto):
        self.proyecto = proyecto
