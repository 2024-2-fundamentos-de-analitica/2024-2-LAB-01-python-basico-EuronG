"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    rta = {}
    rta2 = []

    with open("files/input/data.csv") as file:
        for line in file:
            row = line.split()
            letter = row[0]
            
            if letter not in rta:
                rta[letter] = []
            rta[letter] = rta.get(letter) + [int(row[1])]



    for i in list(rta):
        rta2.append((i, max(rta.get(i)), min(rta.get(i))))
    rta2.sort()
    return rta2



if __name__ == '__main__':
    print(pregunta_05())
