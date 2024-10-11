class Libro:
    def __init__(self, titulo, autor, editorial, categoria, detalle_libro):
        self.titulo = titulo
        self.autor = autor  # Autor object
        self.editorial = editorial  # Editorial object
        self.categoria = categoria  # Categoria object
        self.detalle_libro = detalle_libro  # DetalleLibro object
