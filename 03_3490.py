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

#lista com os n's que iremos testar os algoritmos
casos=[10, 100, 1000, 10000]
v=25   #numero de vezes que iremos testar cada algoritmo

#agora devo fazer a parte em que testo cada um dos algoritmos de ordenação e faço a tabela para ser printada no terminal.


#contagem do tempo de execução de cada algoritmo
ini = time.perf_counter()
end = time.perf_counter()
execucao = end - ini