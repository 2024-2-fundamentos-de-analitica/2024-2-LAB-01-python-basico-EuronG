"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    rta = {}
    rta2 = []

    with open("files/input/data.csv") as file:
        for line in file:
            row = line.split()[-1].split(",")
            
            for i in row:
                kv = i.split(":")
                letter = kv[0]
                if letter not in rta:
                    rta[letter] = []
                rta[letter] = rta.get(letter) + [int(kv[1])]
            



    for i in list(rta):
        rta2.append((i, min(rta.get(i)), max(rta.get(i))))
    rta2.sort()
    return rta2



if __name__ == '__main__':
    print(pregunta_06())
