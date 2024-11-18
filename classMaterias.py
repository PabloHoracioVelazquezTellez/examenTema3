from classCarrera import Carrera
class Materias(Carrera):
    def __init__(self):
        super().__init__()
        self._materias = []

    def getMaterias(self):
        return self._materias

    def setMaterias(self, materias):
        self._materias = materias

    def agregarMateria(self, materia):
        self._materias.append(materia)

    def mostrarMaterias(self):
        return ", ".join(self._materias)
