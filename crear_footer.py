from datetime import datetime

class CrearFooter: 
    @staticmethod                                                   #Funcion que declara un metodo estatico
    def crear_footer():
        año_actual = datetime.now().year
        return f"""
        <footer class="text-center mt-5">
            <p>&copy; {año_actual} - La Fueguina. Todos los derechos reservados.</p>
        </footer>
        """
