import AP_03_ordenacao as ap
import random
import time

#função para uma lista aleatoria de 1 a n
def lista_med(n):
    lista=[]  #lista de 1 ate n, onde iremos reordená-los de forma aleatória
    for i in range(1, n+1):
        lista.append(i)
    mlista=[]
    while len(lista)!=0:
        ind=random.randint(0, len(lista)-1)
        mlista.append(lista[ind])
        lista[ind]=lista[-1]
        lista[-1]=lista[ind]
        del lista[-1]
    return mlista

#função que faz uma lista ordenada de 1 ate n, e depois coloca-na na ordem inversa
def lista_invers(n):
    lista=[]
    for i in range(1, n+1):
        lista.append(i)
    return lista[::-1]

print(lista_invers(10000))