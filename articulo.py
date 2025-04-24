from crear_footer import CrearFooter

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
    
    def to_html_completo(self):
        return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{self.titulo}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">La Fueguina</a>
  </div>
</nav>
<div class="container">
    <div class="card">
        <div class="card-body">
            <h2 class="card-title">{self.titulo}</h2>
            <h4 class="card-subtitle mb-2 text-muted">{self.autor}</h4>
            <p class="card-text">{self.texto}</p>
        </div>
    </div>
    <a href="../articulos.html" class="btn btn-link mt-3">← Volver al índice</a>
</div>
</body>
</html>
"""


    def buscar_palabra(self, palabra_clave):                    #metodo para buscar la palabra clave
        return palabra_clave.lower() in self.texto.lower()
