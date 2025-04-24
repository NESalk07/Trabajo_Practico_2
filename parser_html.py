from articulo import Articulo

class ParserHtml:
    def __init__(self, articulos):                                      #espera una lista de tuplas (titulo, autor, texto)
        self.articulos = []                                             # Inicia la clase y la normaliza
        for titulo, autor, texto in articulos:                          # recorre las tuplas en la lista de articulos
            if titulo.strip() and autor.strip() and texto.strip():      # Titulo, autor y texto no pueden estar vacios
                autor_normalizado = autor.strip().title()               # title() capitaliza el autor
                self.articulos.append(Articulo(titulo, autor_normalizado, texto))   #se crea instancias de la clase articulo
    
    def filtrar_palabra_clave(self, palabra_clave):
        return [articulo for articulo in self.articulos if articulo.buscar_palabra(palabra_clave)]

    def crear_html(self, nombre_archivo='articulos.html'):
        html_inicio= """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Artículos Periodísticos</title>
    <link rel="stylesheet" href="estilos.css">
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
    <header>
        <h1>La Fueguina</h1>
    </header>
    <h1>Artículos Periodísticos</h1>
    <div class="indice">
    <strong>Índice por autor:</strong><br><br>
    <div class="contenedor-articulos">
        """

        html_fin = """
    </div>
    <footer>
        <p>Martes 22 de abril de 2025</p>
    </footer>
</body>
</html>
        """
        articulos_por_autor = {}                                # Agrupar articulos por autor
        for articulo in self.articulos:
            articulos_por_autor.setdefault(articulo.autor, []).append(articulo)

        cuerpo = ""                                             #Indice de autores
        for autor in articulos_por_autor:
            autor_id = autor.lower().replace(" ", "-")
            cuerpo += f'<a href="#{autor_id}">{autor}</a>\n'


            cuerpo += '<div class="contenedor-articulos">\n'

        for autor, articulos in articulos_por_autor.items():    #Articulos por autor.
            autor_id = autor.lower().replace(" ", "-")
            cuerpo += f'<h3 id="{autor_id}">{autor}</h3>\n'
            for articulo in articulos:
                cuerpo += articulo.to_html()
                """
                <div class="articulo">
                    <h2>{titulo}</h2>
                    <p>{texto}</p>
                </div>
                """

        html_completo = html_inicio + cuerpo + html_fin

        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(html_completo)

        print(f"HTML generado exitosamente en '{nombre_archivo}'")
