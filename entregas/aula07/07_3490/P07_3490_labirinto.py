import random as rd

def criar_labrinto(l, c, room='0', wall='1', cheese='*'):
    #crio a matriz com celulas de l linhas e c colunas
    labrinto=[]
    for _ in range(2*l +1):
        labrinto.append([wall]*(2*c +1))
    
    def dfs(x, y):

        labrinto[2*x+1][2*y+1]= room

        pilha_visitados =[(2*x+1, 2*y+1)]

        while pilha_visitados:
            dx, dy=pilha_visitados[-1]
            vizinhos=[(dx, dy+2), (dx, dy-2), (dx+2, dy), (dx-2, dy)]
            rd.shuffle(vizinhos)
            vizi_val=[]
            for vx, vy in vizinhos: #realizo a verificação se um vizinho é válido
                if 0<=vx<(2*l+1) and 0<=vy<(2*c+1) and labrinto[vx][vy]==wall:
                    vizi_val.append((vx,vy)) #coloco esse vizinho válido (dentro do grid, referencia uma wall)

            if vizi_val: #executa a ação, apenas se a lista não estiver vazia, (len!=0 entao True)    
                nx, ny=vizi_val[0] #nx, ny são vizinhos de dx, dy logo são coorde impares
                labrinto[(nx+dx)//2][(ny+dy)//2]=room
                labrinto[nx][ny]=room #coord do vizinho válido que agora é sala
                pilha_visitados.append((nx, ny))
            else:
                del pilha_visitados[-1]

    dfs(0,0)
                
    #parte para colocar o queijo aleatoriamente
    while True:
        queijo_x=int(rd.uniform(0, 2*l))
        queijo_y=int(rd.uniform(0, 2*c))
        if labrinto[queijo_x][queijo_y]==room:
            labrinto[queijo_x][queijo_y]=cheese
            break


    return labrinto

def busca_em_profundidade(labrnto, lin, col, parede="W", quejo="*"):
    pila_visit=[(1, 1)] #lista com as coordenadas na ordem de percorrimento
    visitados={(1, 1)}
    queijo=()
    achou=False
    while pila_visit and not achou: #laço infinito para andar pelo labirinto ate achar o quejo, dai o break
        vx, vy=pila_visit[-1]
        #aqui o vx, vy quer dizer o vértice inicial de busca, enquanto que x, y é o vizinho que esta sendo visitado
        vizinh=[(vx, vy+1), (vx, vy-1), (vx-1, vy), (vx+1, vy)] #as 4 direções para as quais o vertc centro pode ir (em 1 unidade)
        # rd.shuffle(vizinh)
        vizi_prox=False
        for x, y in vizinh:
            if 0<=x<2*lin+1 and 0<=y<2*col+1 and ((x, y) not in visitados):
                visitados.add((x, y))
                if labrnto[x][y]==parede: #achei o fim de um caminho
                    continue
                elif labrnto[x][y]==quejo:
                    achou=True
                    pila_visit.append((x, y))
                    vizi_prox=True
                    queijo=(x, y)
                    break
                else:
                    #primeiro vizinho válido não visitado que está dentro, não é parede nem queijo 
                    pila_visit.append((x, y))
                    vizi_prox=True
                    break
        if vizi_prox==False:  
            #isso indica que (x, y) não possui vizinhos válidos para se andar, então vamos para o vertice anterior a ele
            #com isso, usamos o del para tirá-lo da lista de itens que foram visitados
            del pila_visit[-1]
            continue
    
    for i, j in pila_visit:
        if labrnto[i][j]=="*":
            continue
        else:
            labrnto[i][j]="."

    return labrnto


def print_labrintoe(labrintoe):
    for row in labrintoe:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    mazer = criar_labrinto(m, n)
    print('\nMaze 1')
    print_labrintoe(mazer)
    

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = criar_labrinto(m, n, room, wall, cheese)

    print('\nMaze 2')
    print_labrintoe(maze)
    casa=busca_em_profundidade(maze, m, n)
    print()
    print('Maze com o caminho até o queijo')
    print_labrintoe(casa)
    
