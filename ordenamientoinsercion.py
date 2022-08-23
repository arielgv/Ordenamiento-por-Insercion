# Ordenamiento por inserción
    #recibe una lista desordenada y devuelve la lista ordenada. por el metodo de Ordenamiento por Inserción

import random

def insercion(lista):


    for i in range(0,len(lista)):
        jj = i 
        while jj != 0:
            if lista[i] < lista[i-1]:
                lista[i-1],lista[i]=lista[i],lista[i-1]
            i -=1
            jj = i
    return lista


if __name__=="__main__":

    randomlist = [random.randint(1,100) for i in range (5)]
    print(randomlist)
    print(insercion(randomlist))
