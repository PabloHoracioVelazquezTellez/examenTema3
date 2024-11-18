from classUbicacion import Ubicacion
from classCarrera import Carrera
from classSemestre import Semestre
from classMaterias import Materias
class Edificio(Ubicacion, Carrera):
    def __init__(self):
        Ubicacion.__init__(self)
        Carrera.__init__(self)
        self._nombreEdificio = ""
        self._semestre = Semestre()
        self._materias = Materias()

    def getNombreEdificio(self):
        return self._nombreEdificio

    def setNombreEdificio(self, nombreEdificio):
        self._nombreEdificio = nombreEdificio

    def setNumeroSemestre(self, numeroSemestre):
        self._semestre.setNumeroSemestre(numeroSemestre)

    def getNumeroSemestre(self):
        return self._semestre.getNumeroSemestre()

    def setMaterias(self, materias):
        self._materias.setMaterias(materias)

    def getMaterias(self):
        return self._materias.getMaterias()

    def mostrarM(self):
        return self._materias.mostrarMaterias()

    def mostrarEdificio(self):
        return f"{self._nombreEdificio}"

