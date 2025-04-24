class Articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = autor.strip().title()
        self.texto = texto.strip()

    def to_html(self):
        resumen = self.texto[:300] + "…" if len(self.texto) > 300 else self.texto    # Corta el texto en 300 caracteres
        return f"""
        <div class="articulo">
            <h2>{self.titulo}</h2>
            <p>{self.texto}</p>
            <p>{resumen}</p>
        </div>
        """
    
    def buscar_palabra(self, palabra_clave):                    #metodo para buscar la palabra clave
        return palabra_clave.lower() in self.texto.lower()
