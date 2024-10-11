class TipoUsuario:
    TIPOS_VALIDOS = ["usuario", "administrador"]

    def __init__(self, tipo):
        if tipo.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de usuario no válido: {tipo}. Los tipos permitidos son: {self.TIPOS_VALIDOS}")
        self.tipo = tipo.lower()

    def __str__(self):
        return self.tipo
