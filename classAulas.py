from classEdificio import Edificio
class Aulas(Edificio):
    def __init__(self):
        super().__init__()
        self._numeroAula = ""

    def getNumeroAula(self):
        return self._numeroAula

    def setNumeroAula(self, numeroAula):
        self._numeroAula = numeroAula

    def informacionAula(self):
        if self._semestre.getNumeroSemestre() !=  "Segundo":
            return "Datos no disponibles para la versión del programa."
        aulas_validas = {
            "L": ["5", "4", "6"],
            "H": ["3"],
            "G": ["4"],
            "Y": ["LMAC"]
        }
        if self.getNombreEdificio() not in aulas_validas or self.getNumeroAula() not in aulas_validas[
            self.getNombreEdificio()]:
            return "Datos no disponibles para la versión del programa"
        materia_asignada = "No asignada"

        if self.getNombreEdificio() == "Y" and self.getNumeroAula() == "LMAC":
            materia_asignada = self._materias.getMaterias()[5]
        elif self.getNombreEdificio() == "L" and self.getNumeroAula() == "5":
            materia_asignada = self._materias.getMaterias()[0]
        elif self.getNombreEdificio() == "L" and self.getNumeroAula() == "4":
            materia_asignada = self._materias.getMaterias()[1]
        elif self.getNombreEdificio() == "L" and self.getNumeroAula() == "6":
            materia_asignada = self._materias.getMaterias()[2]
        elif self.getNombreEdificio() == "H" and self.getNumeroAula() == "3":
            materia_asignada = self._materias.getMaterias()[3]
        elif self.getNombreEdificio() == "G" and self.getNumeroAula() == "4":
            materia_asignada = self._materias.getMaterias()[4]

        dataC=Edificio.mostrarInformacionC(self)
        return (f"{dataC}\n"
                f"Semestre: {self._semestre.getNumeroSemestre()}\n"
                f"Edificio: {self.getNombreEdificio()}, Ubicación: {self.getUbicacionEdificio()}\n"
                f"Aula: {self.getNumeroAula()}, Materia en el aula: {materia_asignada}")

    def mostrarAula(self):
        return f"{self._numeroAula}"



