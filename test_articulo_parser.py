from articulo import Articulo
from parser_html import ParserHtml
from excepciones import ArticuloInvalidoError

def test_articulo_to_html():                                                                # Test de preba
    a = Articulo("Título de prueba", "Juan Pérez", "Este es el contenido del artículo.")    # Verifica que se genere el HTML de un articulo
    html = a.to_html()                                                                      # los asset verifican que tenga el titulo esperado
    assert "<h2>Título de prueba</h2>" in html                                              
    assert "Juan Pérez" not in html  
    assert "Este es el contenido del artículo." in html

def test_articulo_buscar_palabra():                                         # Test para probar el metodo-
    a = Articulo("Ejemplo", "Ana Gómez", "Este es un texto para buscar.")   # -que busca una palabra en el texto
    assert a.buscar_palabra("texto")
    assert not a.buscar_palabra("inexistente")

def test_articulo_invalido():                               # Test si el titulo es muy corto
    try:                                                    # o el texto es demasiado corto
        ParserHtml([("Corto", "Autor", "Texto")])  
    except ArticuloInvalidoError as e:
        assert "El título es demasiado corto" in str(e)

    try:
        ParserHtml([("Título válido", "Autor", "Corto")])  
    except ArticuloInvalidoError as e:
        assert "El texto es demasiado corto" in str(e)

def test_parser_slugify():                                                      # test para probar que el metodo convieta todo el texto
    parser = ParserHtml([("Título válido", "Autor", "Texto válido y largo")])   # en texto sin espacios, sin simbolos
    assert parser._slugify("Título de Prueba!") == "titulo-de-prueba"

def test_parser_filtrado_palabra():                                         # test del filtrado de palabras
    articulos = [
        ("Título Uno", "Carlos García", "Texto que contiene la palabra clave."),
        ("Título Dos", "Laura Pérez", "Este no contiene nada.")
    ]
    parser = ParserHtml(articulos)
    filtrados = parser.filtrar_palabra_clave("clave")
    assert len(filtrados) == 1
    assert filtrados[0].titulo == "Título Uno"

if __name__ == "__main__":
    test_articulo_to_html()
    test_articulo_buscar_palabra()
    test_articulo_invalido()
    test_parser_slugify()
    test_parser_filtrado_palabra()
    print(" Pruebas ejecutadas correctamente.")
