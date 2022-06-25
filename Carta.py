class Carta:

    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __eq__(self, other):
        if not isinstance(other, Carta):
            return False
        return self.palo == other.palo and self.numero == other.numero

    def __str__(self):
        return f"Carta: Palo {self.palo}, numero: {self.numero}"
