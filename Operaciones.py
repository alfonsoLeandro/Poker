from math import factorial


def combinatoria(total, grupos_de):
    return (factorial(total) /
            (factorial(total - grupos_de) * factorial(grupos_de)))
