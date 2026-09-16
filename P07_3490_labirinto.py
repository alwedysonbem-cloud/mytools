import random as rd

def criar_labrinto(l, c, room=' ', wall='W', cheese='*'):

    #lista das direções que posso correr
    #direct=[(-2, 0), (2, 0), (0, 2), (0, -2)]

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

def print_labrintoe(labrintoe):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in labrintoe:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    rd.seed(10110)
    mazer = criar_labrinto(m, n)
    print_labrintoe(mazer)
    print('Maze 1')

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = criar_labrinto(m, n, room, wall, cheese)
    print_labrintoe(maze)
    print('\nMaze 2')