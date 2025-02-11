"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    rta = {}

    with open("files/input/data.csv") as file:
        for line in file:
            row = line.split()
            for value in row[4].split(","):
                value = int(value.split(":")[-1])
                rta[row[0]] = rta.get(row[0], 0) + value




    return dict(sorted(rta.items()))



if __name__ == '__main__':
    print(pregunta_12())
