from w06_3490_pilha_encadeada import PilhaEncadeada
from w06_3490_pilha_encadeada import No

class FilaEncadeada:
    def __init__(self):
        self.entrada=PilhaEncadeada()  #Tubo de entrada (parte de cima da Pilha dupla)
        self.saida=PilhaEncadeada()    #Tubo de saida (parte de baixo da Pilha dupla)
        self.tamanho=0        

    def enfileirar(self, item):  #vamos adicionar elementos no tubo superior
        """Adicionamos um item no final da fila, da mesma forma que o método push da classe 
        PilhaEncadeada e através dele, temos que sua complexidade de tempo equivale a O(1)"""
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
        """Retorna o item da frente sem removê-lo; levanta IndexError se a fila estiver vazia.
        Complexidade Temporal:
        \u2014Pior caso: O(n), quando a pilha de saída está vazia e requer a transferência dos n elementos da entrada.
        \u2014Amortizada: O(1), pois cada elemento é transferido para a saída apenas uma única vez ao longo de seu ciclo de vida.
        """
        if self.esta_vazio():
            raise IndexError("Objeto vazio")
        elif not self.saida.esta_vazia():
            return self.saida.topo()
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        return self.saida.topo()
    def esta_vazio(self):
        """Retorna True quando não há elementos armazenados, e False caso contrário.
        Sendo assim, realiza-se no máximo 3 passos e, como efeito, complexidade de
        tempo de O(1)."""
        if self.saida.esta_vazia() and self.entrada.esta_vazia():
            return True
        return False
    def __len__(self):
        """Retornamos um valor do tipo "int" que é a quantidade de itens na fila.
        Nesse sentido, a fim de verificar o tamanho, retornamos apenas self.tamanho,
        executa-se apenas 1 passo, e então tem-se O(1) para todo N."""
        return self.tamanho

    def __repr__(self):
        """Representação textual legível, da frente para o fim.
        \u2014Pior caso: quando todos os itens estão na pilha de entrada;
        para essa situação temos que transferir todos os itens para a pilha de saida, e
        após isso, através de um laço colocar todos os itens da pilha de saida em uma f-string
        para retornarmos a """
        if self.esta_vazio():
            return f"inicio → {None} ← fim"
        
        frase=f"inicio → "
        if not self.saida.esta_vazia():   #se a pilha de saida já contem itens, eles já são printados
            ponteiro=self.saida.top
            while ponteiro is not None:
                frase+=f"{ponteiro.dado} → "
                ponteiro=ponteiro.proximo

        itens=PilhaEncadeada()  #pilha com os itens de cima invertidos
        if not self.entrada.esta_vazia():   #aqui adicionamos todos os itens da pilha de entrada na de saida
            #tirar os elementos de cima e colocalos em algum lugar para depois 
            atual=self.entrada.top
            while atual is not None:
                itens.push(atual.dado)
                atual=atual.proximo

        actual=itens.top
        while not itens.esta_vazia():
            frase+=f"{itens.pop()} → "
            if len(itens)==0:
                break

        frase+=f"{None} ← fim"
        return frase