from classUniversidad import Universidad
class Carrera(Universidad):
    def __init__(self):
        super().__init__()
        self._nombreCarrera = ""

    def getNombreCarrera(self):
        return self._nombreCarrera if self._nombreCarrera else "No especificada"

    def setNombreCarrera(self, nombreCarrera):
        self._nombreCarrera = nombreCarrera

    def mostrarNombreCarrera(self):
        return f"{self._nombreCarrera}\n"

    def mostrarInformacionC(self):
        uData=Universidad.mostrarInformacionU(self)
        return f"{uData}\nCarrera: {self._nombreCarrera}"