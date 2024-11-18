from classAulas import Aulas
def main():
    aula = Aulas()
    aula.setNombre("Instituto Tecnologico de Pachuca")
    aula.setUbicacion("Pachuca Hidalgo")
    aula.setNombreCarrera("Ingenieria en Sistemas Computacionales")
    aula.setNumeroSemestre("Segundo")
    aula.setNombreEdificio("Y")
    aula.setUbicacionEdificio("Zona sureste del plantel")
    aula.setNumeroAula("LMAC")
    aula.setMaterias(["Cálculo Integral", "Álgebra Lineal", "Probabilidad y Estadística", "Química", "Contabilidad", "POO"])
    print(aula.informacionAula())


    """print(aula.mostrarInformacionU())
    print(aula.mostrarAula())
    print(aula.mostrarUbicacion())
    print(aula.getNumeroSemestre())
    print(aula.mostrarEdificio())
    print(aula.mostrarM())"""

if __name__ == "__main__":
    main()
