# Clase Registro de tiempo para los empleados
class RegistroTiempo:
    def __init__(self, fecha, horas_trabajadas, descripcion_tarea, empleado, proyecto):
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion_tarea = descripcion_tarea
        self.empleado = empleado
        self.proyecto = proyecto