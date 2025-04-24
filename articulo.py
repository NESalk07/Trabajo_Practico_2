from crear_footer import CrearFooter

class Articulo:
    def __init__(self, titulo, autor, texto):
        self.titulo = titulo.strip()
        self.autor = autor.strip().title()
        self.texto = texto.strip()

    def to_html(self):
        resumen = self.texto[:300] + "…" if len(self.texto) > 300 else self.texto
        return f"""
        <div class="articulo">
            <h2>{self.titulo}</h2>
            <p>{self.texto}</p>
            <p>{resumen}</p>
        </div>
        """

    def to_html_completo(self, enlace_anterior=None, enlace_siguiente=None):
        navegacion = '<div class="mt-4">'
        if enlace_anterior:
            navegacion += f'<a class="btn btn-outline-secondary me-2" href="{enlace_anterior}">← Anterior</a>'
        if enlace_siguiente:
            navegacion += f'<a class="btn btn-outline-secondary" href="{enlace_siguiente}">Siguiente →</a>'
        navegacion += '</div>'
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
  <div class="container">
    <a class="navbar-brand" href="#">La Fueguina</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContenido" aria-controls="navbarContenido" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarContenido">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="../articulos.html">Inicio</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<div class="container">
    <div class="card mb-4">
        <div class="card-body">
            <h2 class="card-title">{self.titulo}</h2>
            <h4 class="card-subtitle mb-3 text-muted">{self.autor}</h4>
            <p class="card-text">{self.texto}</p>
            {navegacion}
        </div>
    </div>
    <a href="../articulos.html" class="btn btn-outline-secondary">← Volver al índice</a>
</div>

{CrearFooter.crear_footer()}

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    
    def buscar_palabra(self, palabra_clave):
        return palabra_clave.lower() in self.texto.lower()
