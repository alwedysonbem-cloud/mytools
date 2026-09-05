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
    def desenfileirar(self):    #aqui vamos transfeir os elementos do tubo de cima para o de baixo em um laço, e assim tirar o ultimo do tubo de cima
        if self.saida.esta_vazia(): #verifico se a pilha de saida esta vazia (se sim, vemos se a de entrada tem itens para serem removidos)
            if self.entrada.esta_vazia():
                raise IndexError("Objeto vazio")
        while not self.entrada.esta_vazia(): #aqui, removo todos os itens da pilha de cima e os insiro na de baixo
            self.saida.push(self.entrada.pop())    
        valor=self.saida.pop()
        self.tamanho-=1
        return valor
    def frente(self):   #caso em que a pilha de saída está vazia e precisa ser abastecida pela entrada antes de ler o topo
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        self.saida.topo()
    def esta_vazio(self):
        if self.saida.esta_vazia() and self.entrada.esta_vazia():
            return True
        return False
    def __len__(self):
        return self.tamanho
    def __repr__(self):
        frase=f"inicio "
        if self.saida.tamanho != self.tamanho:  #se diferente do tamanho da pilha entao ela nao tem elementos que estao na outra pilha
            if self.entrada.esta_vazia():
                return f"inicio→{None}←fim"
            while not self.entrada.esta_vazia: #aqui, removo todos os itens da pilha de cima e os insiro na de baixo
                self.saida.push(self.entrada.pop())
        
        
        #Aqui já tenho a minha pilha de saida com todos os itens da fila
        ponteiro=self.saida.top
        while ponteiro is not None:
            valor=ponteiro.dado
            frase+=f"→ {valor} "
            ponteiro=ponteiro.proximo
        frase+=f" ← fim"
        return frase

teste=FilaEncadeada()
print(teste)
teste.enfileirar(12)
teste.enfileirar(21)
teste.enfileirar("Wedyson")
print(teste)
teste.desenfileirar()
teste.desenfileirar()
print(teste)
teste.enfileirar("Douglas")
print(teste)