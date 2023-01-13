import random, time


def busqueda_ingenua(lista, objetivo):
    #range(len(lista)) -> 0, 1, 2, 3, ..., len(lista)-1
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    #si no se encuentra el objetivo retornamos -1 porque no es un indice valido
    return -1

#para utilizar la busqueda binaria, la lista debe estar organizada de manera ascendente
def busqueda_binaria(lista, objetivo, liminite_inferior = None, limite_superior = None):
    if liminite_inferior is None:
        liminite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista)-1

    if limite_superior < liminite_inferior:
        return -1
    
    punto_medio = (liminite_inferior + limite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista , objetivo, liminite_inferior, punto_medio-1 )
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)


if __name__ == '__main__':
    size = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < size:
        conjunto_inicial.add(random.randint(-3*size, 3*size))
    
    lista = sorted(list(conjunto_inicial))
    
    #midiendo el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista:
        busqueda_ingenua(lista, objetivo)
    fin = time.time()
    print("Tiempo de busqueda ingenua: ", fin-inicio)

    #midiendo el tiempo de busqueda binaria
    inicio = time.time()
    for objetivo in lista:
        busqueda_binaria(lista, objetivo)
    fin = time.time()
    print("Tiempo de busqueda binaria: ", fin-inicio)