class Ubicacion:
    def __init__(self):
        self._ubicacionEdificio = ""

    def getUbicacionEdificio(self):
        return self._ubicacionEdificio if self._ubicacionEdificio else "No especificada"

    def setUbicacionEdificio(self, ubicacionEdificio):
        self._ubicacionEdificio = ubicacionEdificio

    def mostrarUbicacion(self):
       return f"{self._ubicacionEdificio}"