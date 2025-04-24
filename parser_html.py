import os
from articulo import Articulo
from crear_footer import CrearFooter

class ParserHtml:
    def __init__(self, articulos):                                                  # espera una lista de tuplas (titulo, autor, texto)
        self.articulos = []                                                         # Inicia la clase y la normaliza
        for titulo, autor, texto in articulos:                                      # recorre las tuplas en la lista de articulos
            if titulo.strip() and autor.strip() and texto.strip():                  # Titulo, autor y texto no pueden estar vacios
                autor_normalizado = autor.strip().title()                           # title() capitaliza el autor
                self.articulos.append(Articulo(titulo, autor_normalizado, texto))   # se crea instancias de la clase articulo
    
    def _slugify(self, texto):
        import re
        texto = texto.lower()
        texto = re.sub(r'\W+', '-', texto)
        return texto.strip('-')

    def filtrar_palabra_clave(self, palabra_clave):
        return [articulo for articulo in self.articulos if articulo.buscar_palabra(palabra_clave)]
    
    def crear_paginas_articulos(self, carpeta='articulos'):
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

            for i, articulo in enumerate(self.articulos):
                nombre_archivo = f"{carpeta}/articulo_{i+1}.html"
                with open(nombre_archivo, 'w', encoding='utf-8') as f:
                    f.write(articulo.to_html_completo())

    def crear_html(self, nombre_archivo='articulos.html'):
        html_inicio= """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Artículos Periodísticos</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            color: #333;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 40px;
        }

        .contenedor-articulos {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .articulo {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .articulo h2 {
            margin-top: 0;
            color: #1a73e8;
        }

        .articulo h4 {
            margin: 5px 0 10px;
            color: #555;
        }

        .articulo p {
            line-height: 1.6;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">La Fueguina</a>
    </div>
</nav>
    <div class="container">
        <h1 class="text-center mb-4">Artículos Periodísticos</h1>
        <div class="mb-4">
            <h5>Índice por autor:</h5>
    """
        
        html_fin = f"""
        </div>
{CrearFooter.crear_footer()}                                    <!-- Se llama al metodo crear_footer de la clase CrearFooter-->
</body>
</html>
        """
        articulos_por_autor = {}                                # Agrupar articulos por autor
        for articulo in self.articulos:
            articulos_por_autor.setdefault(articulo.autor, []).append(articulo)

        cuerpo = ""                                             #Indice de autores
        for autor in articulos_por_autor:
            autor_id = autor.lower().replace(" ", "-")
            cuerpo += f'<a class="btn btn-outline-primary btn-sm m-1" href="#{autor_id}">{autor}</a>\n'

        for autor, articulos in articulos_por_autor.items():
            autor_id = autor.lower().replace(" ", "-")
            cuerpo += f'<hr><h2 id="{autor_id}">{autor}</h2>\n'
            cuerpo += '<div class="row">\n'

            for i, articulo in enumerate(articulos):
                index = self.articulos.index(articulo) + 1
                link = f"articulos/articulo_{index}.html"
                cuerpo += f"""
            <div class=\"col-md-4 mb-4\">
                <div class=\"card h-100\">
                <div class=\"card-body\">
                <h5 class=\"card-title\"><a href=\"{link}\">{articulo.titulo}</a></h5>
                <h6 class=\"card-subtitle mb-2 text-muted\">{articulo.autor}</h6>
                <p class=\"card-text\">{articulo.texto[:300]}...</p>
                <a href=\"{link}\" class=\"btn btn-primary\">Leer más</a>           <!-- Me muestra todo el texto del articulo -->
            </div>
        </div>
    </div>
    """
                if (i + 1) % 3 == 0:                            # cada e articulos cierra y abre una nueva fila
                    cuerpo += '</div><div class="row">\n'

            cuerpo += '</div>\n'                                # cierra la ultima fila

        html_completo = html_inicio + cuerpo + html_fin

        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(html_completo)

        print(f"HTML generado exitosamente en '{nombre_archivo}'")
