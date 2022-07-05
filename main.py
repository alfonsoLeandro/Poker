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
    print(f"Palo '{inpt}' no reconocido. Usando ROMBO")
    return Palo.ROMBO


def getNumero(inpt):
    if not inpt.isnumeric():
        print(f"El numero '{inpt}' no existe, usando 1 como numero por defecto.")
        return 1
    numero = int(inpt)
    if numero > 13 or numero < 1:
        numero = randint(1, 12)
        print(f"El numero debe ser mayor a 0 y menor a 13, usando {numero}")
    return numero


class Program:

    def __init__(self):
        print("palos disponibles: ROMBO, PICAS, CORAZONES, TREBOL")
        print("números disponibles: 1 al 13. 1 es el AS, 11 es la sota, 12 es la reina, 13 es el rey.")
        self.carta1 = Carta(getPalo(input("Palo de primer carta:")),
                            getNumero(input("Numero de primer carta:")))
        self.carta2 = Carta(getPalo(input("Palo de segunda carta:")),
                            getNumero(input("Numero de segunda carta:")))

        if self.carta1 == self.carta2:
            print("Las dos cartas no pueden ser iguales.")
            return

        print()
        print(f"carta 1: {self.carta1}")
        print(f"carta 2: {self.carta2}")
        print()

        probabilidad_color = "{:.2f}%".format(self.calcular_posibilidades_color() * 100)
        probabilidad_escalera_real = "{:.2f}%".format(self.calcular_posibilidades_escalera_real() * 100)

        if probabilidad_color == "0.00%":
            probabilidad_color = "Muy pequeña (menor a 0.01%)"

        if probabilidad_escalera_real == "0.00%":
            probabilidad_escalera_real = "Muy pequeña (menor a 0.01%)"

        print(f"Probabilidad de tener color: {probabilidad_color}.")
        print(f"Probabilidad de tener escalera real: {probabilidad_escalera_real}.")
        print()

    def calcular_posibilidades_color(self):
        if self.carta1.palo == self.carta2.palo:
            return (
                    ((combinatoria(11, 3)*39*38) / combinatoria(48, 5)) +
                    ((combinatoria(11, 4)*39) / combinatoria(49, 5)) +
                    (combinatoria(11, 5) / combinatoria(50, 5))
            ) + 3 * (combinatoria(13, 5) / combinatoria(50, 5))
        else:
            return 2 * (
                    (combinatoria(12, 4)*38/combinatoria(49, 5)) + (combinatoria(12, 5)/combinatoria(50, 5))
            ) + 2 * (combinatoria(13, 5) / combinatoria(50, 5))

    def calcular_posibilidades_escalera_real(self):
        if self.carta1.numero == 1 or self.carta1.numero > 9:
            if self.carta2.numero == 1 or self.carta2.numero > 9:
                if self.carta1.palo == self.carta2.palo:
                    return (47*46/combinatoria(48, 5)) + 3/combinatoria(50, 5)
                else:
                    return 2 * (46/combinatoria(49, 5)) + 2/combinatoria(50, 5)
            else:
                return (46/combinatoria(49, 5)) + 3/combinatoria(50, 5)
        elif self.carta2.numero == 1 or self.carta2.numero > 9:
            return (46/combinatoria(49, 5)) + 3/combinatoria(50, 5)
        else:
            return 4/combinatoria(50, 5)


if __name__ == '__main__':
    Program()
    print("Programa finalizado")
