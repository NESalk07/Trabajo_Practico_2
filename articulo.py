class Articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = autor.strip().title()
        self.texto = texto.strip()

    def to_html(self):
        return f"""
        <div class="articulo">
            <h2>{self.titulo}</h2>
            <p>{self.texto}</p>
        </div>
        """
