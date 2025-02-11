"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    rta = {}
    rta2 = []

    with open("files/input/data.csv") as file:
        for line in file:
            row = line.split()
            letter = row[0]
            rta[letter] = rta.get(letter, 0) + int(row[1])



    for i in list(rta):
        rta2.append((i, rta.get(i)))
    rta2.sort()
    return rta2



if __name__ == '__main__':
    print(pregunta_03())
