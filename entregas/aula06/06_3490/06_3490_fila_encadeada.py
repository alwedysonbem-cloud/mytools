import importlib

modulo_pilha=importlib.import_module("06_3490_pilha_encadeada")
PilhaEncadeada = modulo_pilha.PilhaEncadeada

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
        """Remove e retorna o item da frente; levanta IndexError se a fila estiver vazia.
        \u2014Pior caso: O(n), cenário, em que a pilha de saida (contem os itens da fila na
        ordem de saida \u2014 os que estão no topo são os primeiros a sair, por terem sido os
        primeiros a entrarem na pilha de entrada \u2014) está vazia. Com isso, transferimos todos os itens 
        da pilha de entrada e após isso usamos self.saida.pop() para retornarmos e removermos o item da
        fila encadeada
        \u2014Armotizado: O(1), quando a pilha de saida não está vazia. Desse modo, usamos o método pop
        da classe PilhaEncadeada para removermos o primeiro item da fila que é o que está no topo
        da pilha de saida."""
        if self.esta_vazia():
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
        if self.esta_vazia():
            raise IndexError("Objeto vazio")
        elif not self.saida.esta_vazia():
            return self.saida.topo()
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        return self.saida.topo()
    def esta_vazia(self):
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
        para retornarmos ela.
        \u2014Melhor caso: quando todos os itens já estão na pilha de saida;
        para esse cenário necessitamos apenas realizar o laço de colocar todos os itens na f-string
        que irá ser retornada no fim.
        Desse modo, veja que em todas as hipóteses a complexidade de tempo é linear, seja n+n, seja
        apenas n, o que nos dá O(n)."""

        if self.esta_vazia():
            return f"inicio → {None} ← fim"
        
        frase=f"inicio → "

        pila_prin=PilhaEncadeada()
        while not self.saida.esta_vazia():      #se a pilha de saida já contem itens, eles já são printados
            frase+=f"{self.saida.topo()} → "
            pila_prin.push(self.saida.pop())

        while not pila_prin.esta_vazia():
            self.saida.push(pila_prin.pop())

        itens=PilhaEncadeada()                  #pilha com os itens de cima invertidos
        while not self.entrada.esta_vazia():
            itens.push(self.entrada.pop())

        while not itens.esta_vazia():
            frase+= f"{itens.topo()} → "
            self.entrada.push(itens.pop())

        frase+=f"{None} ← fim"
        return frase
