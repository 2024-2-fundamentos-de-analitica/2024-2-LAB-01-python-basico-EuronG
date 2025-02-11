"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    rta = {}
    rta2 = []

    with open("files/input/data.csv") as file:
        for line in file:
            letter = line.split()[0]
            rta[letter] = rta.get(letter, 0) + 1



    for i in list(rta):
        rta2.append((i, rta.get(i)))
    rta2.sort()
    return rta2



if __name__ == '__main__':
    print(pregunta_02())