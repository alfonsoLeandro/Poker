from Carta import Carta
from Palo import Palo
from random import randint
from Operaciones import combinatoria


def getPalo(inpt):
    inpt = inpt.lower()
    if inpt == "pica" or inpt == "picas":
        return Palo.PICA
    if inpt == "corazon" or inpt == "corazones":
        return Palo.CORAZON
    if inpt == "trebol" or inpt == "treboles":
        return Palo.TREBOL
    if inpt == "rombo" or inpt == "rombos":
        return Palo.ROMBO
    print(f"Palo {inpt} no reconocido. Usando ROMBO")
    return Palo.ROMBO


def getNumero(inpt):
    numero = int(inpt)
    if numero > 13 or numero < 1:
        numero = randint(1, 12)
        print(f"El numero debe ser mayor a 0 y menor a 13, usando {numero}")
    return numero


class Program:

    def __init__(self):
        self.carta1 = Carta(getPalo(input("Palo de primer carta:")),
                            getNumero(input("Numero de primer carta:")))
        self.carta2 = Carta(getPalo(input("Palo de segunda carta:")),
                            getNumero(input("Numero de segunda carta:")))

        if self.carta1 == self.carta2:
            print("Las dos cartas no pueden ser iguales.")
            return

        print(self.carta1)
        print(self.carta2)

        posibilidades_color = self.calcular_posibilidades_color()
        posibilidades_poker = self.calcular_posibilidades_poker()
        todas_las_posibilidades = combinatoria(52, 5)

        print(f"Cantidad de posibilidades de tener color: {posibilidades_color}."
              f" Probabilidad: {(posibilidades_color/todas_las_posibilidades) * 100}%")
        print(f"Cantidad de posibilidades de tener poker: {posibilidades_poker}."
              f" Probabilidad: {(posibilidades_poker/todas_las_posibilidades) * 100}%")

    def calcular_posibilidades_color(self):
        return 1_000_000

    def calcular_posibilidades_poker(self):
        return 523_000


if __name__ == '__main__':
    Program()
    print("Programa finalizado")
