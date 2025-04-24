from parser_html import ParserHtml                  # se importa la clase ParserHtml
from excepciones import ArticuloInvalidoError       # se importa la excepcion

if __name__ == "__main__":
    articulos = [
        ("Extorcion y desvios de fondos", "Federico Gonzales del Solar", "El juez federal Sebastián "
        "Casanello dispuso elevar a juicio oral la causa que investiga al líder del Polo Obrero, "
        "Eduardo Belliboni, y a más de una docena de otros dirigentes sociales, por el presunto desvío "
        "de fondos destinados a la asistencia social y la supuesta extorsión tanto a los beneficiarios "
        "del exPotenciar Trabajo y como a aquellos que aspiraban a obtener dicha protección. Casanello "
        "rechazó los requerimientos de las defensas y dio por cerrada la etapa de instrucción de una "
        "causa que comenzó a construirse en diciembre de 2023 a partir de una serie de denuncias "
        "realizadas en una línea telefónica que habilitó para esos fines el ministerio de Seguridad, que"
        " conduce Patricia Bullrich.."),
        ("Nuevos aumentos",""," sin autor"),
        ("La ruta del dinero piquetero”: la Justicia reconstruye el recorrido de subsidios, facturas truchas y empresas fantasma", 
         "Camila Dolabjian","En menos de 10 días, el 25 de junio, Eduardo Belliboni deberá presentarse en Comodoro Py a indagatoria "
         "en el juzgado de Sebastián Casanello. El caso del Polo Obrero y su líder es el más avanzado en cuanto a las denuncias que "
         "se realizaron contra los grupos piqueteros, en las que además de haberse reunido prueba sobre extorsiones y amenazas a los "
         "beneficiarios de los planes sociales, se recopiló documentación contundente sobre el manejo de los subsidios que recibían del Estado. "
         "En ese sentido, la Justicia acumuló fuertes indicios de que el dinero salía de las arcas públicas, pasaba a través de un sistema de "
         "cooperativas y empresas fantasmas con facturas truchas y cheques redirigidos, y volvía a los bolsillos de la política.LA NACION mostró "
         "el 30 de mayo las facturas apócrifas que firmaba el propio Belliboni, pero el líder piquetero negó conocer que las empresas "
         "que le prestaban servicios o le vendían productos eran de compañías fantasma. Ahora, LA NACION accedió a una serie de cheques y "
         "posteriores rendiciones al Ministerio de Desarrollo Social que lo complican todavía más, porque la firma de Belliboni aparece en "
         "todo el circuito de dinero. Y revela que los destinatarios finales de los fondos que se pagaban en concepto de computadoras, software "
         "y otros bienes, en realidad, no eran los supuestos vendedores, sino la empresa que está detrás de la propaganda del Partido Obrero. "
         "Estos elementos fueron incorporados como indicios de una ruta del dinero destinada a quedarse con parte del dinero de los subsidios a "
         "través de facturas apócrifas."),
        ("Los sorpresivos vínculos con la política y el poder detrás de la empresa investigada por las facturas truchas del Polo Obrero",""
        "Camila Dolabjian","La investigación por el uso de facturas truchas por parte del Polo Obrero, que hizo foco en el uso de fondos "
        "de los subsidios del Estado, amenaza con destapar una trama más amplia de lavado de dinero, con nexos en la política y figuras "
        "acusadas de corrupción. La empresa Coxtex, una de las empresas que emitió las facturas apócrifas firmadas por Eduardo Belliboni, "
        "muestra vínculos sospechosos con abogados y escribanos vinculados a la política, según una investigación de LA NACION. Coxtex, que "
        "es una sociedad fantasma de acuerdo al expediente que tramita en el juzgado de Sebastián Casanello, operó con el Polo Obrero, que la"
        " habría contratado al menos dos veces, por cerca de $5millones. Sin embargo, los nuevos datos demuestran que no solo actuó con el Polo "
        "Obrero. Al momento en que facturó para la Cooperativa de Trabajo El Resplandor Limitada (del Polo Obrero), Coxtex ya había emitido otras"
        " 535 facturas. Un enorme volumen que demuestra que su actividad iba mucho más allá que el grupo piquetero de izquierda. Meses antes, esas "
        "otras facturas habían hecho sonar alarmas en la AFIP, pero nunca fueron atendidas, ni el CUIT fue suspendido. LA NACION confirmó que el "
        "organismo recaudador ya tenía información de la firma sospechosa en 2020."),
        ("Tips Jurídicos: claves para no ser engañado en un acuerdo", "Juan Bautista Torres Lopez", "De la"
        " mano de este consejo, debe encenderse una sirena mental cuando una de las partes contratantes "
        "busca que la otra parte no acceda a una copia de lo que firmó o va a firmar. Las “razones” para no"
        " entregar una copia de lo suscripto pueden ser variadas: que “no hace falta”, que se va a "
        "entregar con posterioridad (¿qué garantías hay de eso?) o que en orden a la confidencialidad, es "
        "más seguro que no haya dos o tres copias firmadas de un mismo instrumento (pero para esto último "
        "es que se utilizan las llamadas “cláusulas de confidencialidad”). Si alguien no puede llevarse una"
        " copia de lo que firmó (que en definitiva, implica una constancia del compromiso asumido, nada más"
        " y nada menos), a falta de doble ejemplar, poner doble (o triple) atención. “No, tampoco podés "
        "sacarle una foto al contrato”. Si una parte quiere que se firme “ahora mismo” un acuerdo, no "
        "entrega copia del instrumento a suscribir y además impide que se tome una foto de lo que se va a"
        " acordar (lo que permitiría, por ejemplo, que un abogado o abogada lo revise al menos de manera"
        " preliminar), es muy probable que estemos frente a un “acuerdo asimétrico” o un contrato en el que "
        "algo pretende ocultarse o pasarse por alto. Y es que, en definitiva, algunas decisiones -más si son "
        "importantes o a largo plazo- deben poder ser sometidas a revisión o consulta profesional, y si la"
        " “gran oportunidad de negocio” priva de esa chance, habría que preguntarse por qué (y por qué tiene"
        " que ser rápido, y por qué no podría uno llevarse copia de lo que firmó). Lo que se resuelve a la "
        "ligera o se ahorra al comienzo, puede ser un dolor de cabeza a futuro o una fuga de dinero por "
        "imprudencia o exceso de confianza."),
        ("La inteligencia artificial como aliada para las prácticas de estudio en gestión hotelera y turismo",
          "Mariana Kozodij", "Ya son varios los cursos que consideran situaciones, a veces distópicas, que "
          "ponen a los estudiantes en aprietos para pensar posibles soluciones de manera efectiva y ofrecer "
          "respuestas que puedan considerar cruces algorítmicos hasta ahora impensados. El análisis predictivo"
          " de la IA permite evaluar de forma totalmente diferente la experiencia de cada usuario y comprender "
          "mejor los puntos de dolor que podría enfrentar un estudiante de hotelería y/o turismo. En el "
          "mundo real, los aspirantes que desean hacer carrera en este universo se deben enfrentar a "
          "situaciones como la gestión de queja de huéspedes, de problemas de personal, dificultades "
          "financieras e incluso éticas. Todas estas gestiones son cada vez más atravesadas por los "
          "análisis que pueden hacerse a partir del uso de la IA, y las grandes cadenas hoteleras, agencias"
          " de viaje y turismo ya están en pleno uso de estudiar sus potencialidades. Por ejemplo, un reciente"
          " estudio de PWC indica que “cerca del 70% de los consumidores prefiere interactuar con chatbots para "
          "obtener información rápida”; un dato que invita a reflexionar sobre el rol y servicio humano en la "
          "cadena de esta industria..")
    ]


    try:
        parser = ParserHtml(articulos)
        parser.crear_html()                     #Se crea el HTML
    except ArticuloInvalidoError as e:
        print("Error al procesar los articulos: ", e)

    parser.crear_paginas_articulos()        #Se crean las paginas de cada articulo

    palabra = "fondos"
    articulos_filtrados = parser.filtrar_palabra_clave(palabra)

    if articulos_filtrados:
        print(f"Articulos que tienen la palabra '{palabra}'")
        for articulo in articulos_filtrados:
            print(f" - {articulo.titulo} ({articulo.autor})")

        parser_filtrado = ParserHtml([(a.titulo, a.autor,a.texto) for a in articulos_filtrados])
        parser_filtrado.crear_html("articulos_filtrados.html")
    else: 
        print(f"No se encontraron archivos con esa palabra '{palabra}'.")