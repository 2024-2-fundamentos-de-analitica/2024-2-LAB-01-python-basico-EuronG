"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    rta = {}

    with open("files/input/data.csv") as file:
        for line in file:
            row = line.split()
            for letter in row[3].split(","):
                rta[letter] = rta.get(letter, 0) + int(row[1])




    return dict(sorted(rta.items()))



if __name__ == '__main__':
    print(pregunta_11())
