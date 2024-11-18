from classCarrera import Carrera
class Semestre(Carrera):
    def __init__(self):
        super().__init__()
        self._numeroSemestre = 0

    def getNumeroSemestre(self):
        return self._numeroSemestre if self._numeroSemestre else "No especificado"

    def setNumeroSemestre(self, numeroSemestre):
        self._numeroSemestre = numeroSemestre

    def mostrarSemestre(self):
        return f"{self._numeroSemestre} Semestre"
