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
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 30px;
        }}
        .articulo {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        h2 {{ color: #1a73e8; }}
        h4 {{ color: #666; }}
        p {{ line-height: 1.6; }}
        a {{ text-decoration: none; color: #1a73e8; }}
    </style>
</head>
<body>
    <a href="../articulos.html">← Volver al índice</a>      <!-- enlace para volver a la pagina anterior-->
    <div class="articulo">
        <h2>{self.titulo}</h2>
        <h4>{self.autor}</h4>
        <p>{self.texto}</p>
    </div>
</body>
</html>
"""

    def buscar_palabra(self, palabra_clave):                    #metodo para buscar la palabra clave
        return palabra_clave.lower() in self.texto.lower()
