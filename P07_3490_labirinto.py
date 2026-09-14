import random

def criar_labrinto(l, c, room=' ', wall='W', cheese='.'):

    #lista das direções que posso correr
    direct=[(-1, 0), (1, 0), (0, 1), (0, -1)]

    #crio a matriz com celulas de l linhas e c colunas
    labrinto=[]
    for _ in range(2*l +1):
        labrinto.append([wall]*(2*c +1))

    return labrinto