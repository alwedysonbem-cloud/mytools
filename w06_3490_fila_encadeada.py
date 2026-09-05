from w06_3490_pilha_encadeada import PilhaEncadeada
from w06_3490_pilha_encadeada import No

class FilaEncadeada:
    def __init__(self):
        self.entrada=PilhaEncadeada()  #Tubo de entrada (parte de cima da Pilha dupla)
        self.saida=PilhaEncadeada()    #Tubo de saida (parte de baixo da Pilha dupla)
        self.tamanho=0

    def mudar_pilha(self):
        if self.tamanho==self.entrada.tamanho:
            for _ in range(self.entrada.tamanho):
                self.saida.push(self.entrada.pop())
        

    def enfileirar(self, item):  #vamos adicionar elementos no tubo superior
        self.entrada.push(item)
        self.tamanho+=1
    def desenfileirar(self):
        if self.esta_vazio():
            raise IndexError("Objeto vazio")
        elif not self.saida.esta_vazia():  #vejo se a pilha de saida nao estiver vazia
            valor=self.saida.pop()
            self.tamanho-=1
            return valor
        #aqui a pilha de saida vai estar vazia de certeza
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        valor=self.saida.pop()
        self.tamanho-=1
        return valor
    def frente(self):
        if self.esta_vazio():
            raise IndexError("Objeto vazio")
        elif not self.saida.esta_vazia():
            return self.saida.topo()
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        return self.saida.topo()
    def esta_vazio(self):
        if self.saida.esta_vazia() and self.entrada.esta_vazia():
            return True
        return False
    def __len__(self):
        return self.tamanho

    def __repr__(self):
        if self.esta_vazio():
            return f"inicio → {None} ← fim"
        
        frase=f""

        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
