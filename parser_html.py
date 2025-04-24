import os
import re
import unicodedata
from articulo import Articulo
from crear_footer import CrearFooter
from excepciones import ArticuloInvalidoError
from collections import defaultdict

class ParserHtml:
    def __init__(self, articulos):
        self.articulos = []
        for titulo, autor, texto in articulos:
            if not (titulo.strip() and autor.strip() and texto.strip()):
                continue
            if len(titulo.strip()) < 10:
                raise ArticuloInvalidoError(f"El título es demasiado corto: '{titulo}' ")
            if len(texto.strip()) < 10:
                raise ArticuloInvalidoError(f"El texto es demasiado corto para el artículo: '{titulo}' ")

            autor_normalizado = autor.strip().title()
            self.articulos.append(Articulo(titulo, autor_normalizado, texto))

    def _slugify(self, texto):                                                                      #metodo para convertir textos en texto sin espacios, sin acentos, sin símbolos raros
        texto = texto.lower()
        texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
        texto = re.sub(r'\W+', '-', texto)
        return texto.strip('-')

    
    def filtrar_palabra_clave(self, palabra_clave):
        return [articulo for articulo in self.articulos if articulo.buscar_palabra(palabra_clave)]

    def crear_paginas_articulos(self, carpeta='articulos'):             # Indica donde se guarda los HTML de cada articulos
        if not os.path.exists(carpeta):   # Se verifica si ya existe una carpeta
            os.makedirs(carpeta)

        for i, articulo in enumerate(self.articulos):                   # for para crear un HTML por cada articulo
            nombre_archivo = f"{carpeta}/articulo_{i+1}.html"           # nombra a los nuevos HTML como articulo_1/2/3 sucesivamente
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(articulo.to_html_completo())

    def crear_html(self, nombre_archivo='articulos.html'):              # Inicio del metodo que contiene el HTML
        html_inicio = """
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

        .btn-outline-secondary {
            margin-right: 5px;
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
    """

        articulos_por_autor = {}                                        # Agrupa artículos por autor
        for articulo in self.articulos:
            articulos_por_autor.setdefault(articulo.autor, []).append(articulo)

        from collections import defaultdict                             # Agrupa los autores por inicial del apellido
        autores_por_letra = defaultdict(list)
        for autor in articulos_por_autor:
            partes = autor.split()
            if partes:
                inicial = partes[-1][0].upper()
                autores_por_letra[inicial].append(autor)

            # Crea el índice alfabético (solo letras con autores)
        indice_letras = '<div class="mb-4"><h5>Filtrar por inicial del apellido:</h5>\n<div class="d-flex flex-wrap gap-2">\n'
        for letra in sorted(autores_por_letra):
            indice_letras += f'<a class="btn btn-outline-secondary btn-sm" href="#letra-{letra}">{letra}</a>\n'
        indice_letras += '</div></div>\n'

        tabla_resumen = """                                             <!--Crea tabla resumen (cantidad de artículos por autor)-->                                         
            <h5 class="mt-4">Cantidad de artículos por autor</h5>
            <table class="table table-striped table-bordered">
            <thead class="table-dark">
            <tr>
                <th>Autor</th>
                <th>Artículos</th>
            </tr>
            </thead>
            <tbody>
        """
        for autor, lista_articulos in articulos_por_autor.items():
            tabla_resumen += f"""
            <tr>
                <td>{autor}</td>
                <td>{len(lista_articulos)}</td>
            </tr>
            """
        tabla_resumen += """
            </tbody>
        </table>
        """

          # Crear el índice de autores con sus letras
        cuerpo = ""                                                                     # Índice de autores
        letra_actual = ""
        for autor, articulos in sorted(articulos_por_autor.items(), key=lambda x: x[0].split()[-1]):
            letra = autor.split()[-1][0].upper()
            if letra != letra_actual:
                cuerpo += f'<hr><h2 id="letra-{letra}">Autores con "{letra}"</h2>\n'
                letra_actual = letra

            autor_id = autor.lower().replace(" ", "-")
            cuerpo += f'<h3 id="{autor_id}">{autor}</h3>\n'
            cuerpo += '<div class="row">\n'

            for i, articulo in enumerate(articulos):
                index = self.articulos.index(articulo) + 1
                link = f"articulos/articulo_{index}.html"
                cuerpo += f"""
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><a href="{link}">{articulo.titulo}</a></h5>
                            <h6 class="card-subtitle mb-2 text-muted">{articulo.autor}</h6>
                            <p class="card-text">{articulo.texto[:300]}...</p>
                            <a href="{link}" class="btn btn-primary">Leer más</a>
                        </div>
                    </div>
                </div>
                """
                if (i + 1) % 3 == 0:
                    cuerpo += '</div><div class="row">\n'
            cuerpo += '</div>\n'


        html_completo = html_inicio + indice_letras + tabla_resumen + cuerpo + CrearFooter.crear_footer() + "</body></html>"

        with open(nombre_archivo, 'w', encoding='utf-8') as f:           # Guardar el archivo HTML
            f.write(html_completo)

        print(f"HTML generado exitosamente en '{nombre_archivo}'")
