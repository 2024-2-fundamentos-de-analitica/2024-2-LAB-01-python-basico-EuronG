"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    col = 0
    with open("files/input/data.csv") as file:
        for line in file:
            col += int(line.split()[1])
    return col



if __name__ == '__main__':
    print(pregunta_01())