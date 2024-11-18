class Universidad:
    def __init__(self):
        self._nombre = ""
        self._ubicacion = ""

    def getNombre(self):
        return self._nombre if self._nombre else "No especificado"

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion if self._ubicacion else "No especificada"

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def mostrarInformacionU(self):
        return f"universidad: {self._nombre}, Ubicacion: {self._ubicacion}"