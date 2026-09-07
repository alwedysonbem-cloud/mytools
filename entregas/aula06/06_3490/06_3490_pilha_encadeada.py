class No:
        def __init__(self, dado):
            """ Essa função serve para:
            \u2014instanciar a classe No, que nos dá um nó com
            seu valor e um ponteiro para o próximo nó
            \u2014self.dado: referência para o valor armazenado
            na mémoria;
            \u2014self.proximo: referência para o proximo nó."""
            self.dado = dado
            self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        """Def para instanciar uma pilha encadeada:
        \u2014self.top: referência para o topo da pilha;
        \u2014self.tamanho: variável que guarda o tamanho
        da pilha durante todas as operações"""
        self.top = None
        self.tamanho = 0
    def push(self, dado):
        """Cria um novo nó "new", onde new.dado é o novo item
        adicionado na pilha encadeada:
        faz com que new.proximo aponte para o antigo topo, e faz com que
        self.top (ponteiro que indica o topo da pilha) referencie new (que
        é um No para o item adicionado);
        por fim atualizamos o tamanho da pilha encadeada
        Portanto, para adicionar qualquer item, levamos um tempo constante de 4 passos, ou seja,
        O(1) para adicionar"""
        new=No(dado)
        new.proximo=self.top
        self.top=new
        self.tamanho+=1
    def pop(self):
        """Verifica-se se a pilha está vazia (se seu topo aponta para None)
        e assim levantamos IndexError.
        Caso ela não esteja vazia, guardamos o valor do topo (que será removido),
        fazemos com que o ponteiro do topo aponte para self.top.proximo (que é uma referência para
        o item em seguida do topo), reduzimos self.tamanho em -1 e, por fim, retornamos o valor
        do topo.
        Assim, para removermos um item de uma pilha temos no máximo um tempo de 5 passos, resultando
        em O(1) para uso do método pop()"""
        if self.top==None:
            raise IndexError("Objeto vazio")
        dado_removido=self.top.dado
        self.top=self.top.proximo
        self.tamanho-=1
        return dado_removido
    def topo(self):
        """Se a pilha é vazia, levantamos o erro IndexError usando a mesma ideia do pop
        (ponteiro do topo apontar para None, indica que a pilha está vazia pois não
        possui elementos no topo).
        Se não está vazia, retornamos o valor do nó do topo (self.top.dado).
        Dessa forma, para vermos qual dado está armazenado no topo, leva-se um tempo de no máximo
        2 passos, levando a uma complexidade de O(1)"""
        if self.top==None:
            raise IndexError("Objeto vazio")
        return self.top.dado
    def esta_vazia(self):
        """Retornamos True se a pilha está vazia ou False caso contrário.
        Sendo assim, realiza-se no máximo 3 passos e, como efeito, complexidade de
        tempo de O(1)."""
        if self.top is None:
            return True
        else:
            return False
    def __len__(self):
        """Retornamos um valor do tipo "int" que é a quantidade de itens na pilha.
        Nesse sentido, a fim de verificar o tamanho, retornamos apenas self.tamanho,
        executa-se apenas 1 passo, e então tem-se O(1) para todo N."""
        return self.tamanho
    def __repr__(self):
        """Retornamos uma f-string contendo uma representação do topo para a base do da pilha.
        Observando que estamos a percorrer toda a pilha, temos um laço que verifica se o ponteiro
        é None, isto é, vemos se o valor atual é o ultimo ou se a pilha é vazia. Desse modo, temos
        que a execução em n passos (com n sendo a quantidade de itens na pilha), resultando numa
        complexidade de O(n)."""
        ponteiro=self.top  #pra onde o meu ponteiro aponta atualmente (inicialmente no topo)
        frase=f""
        while ponteiro is not None:
            frase+=f"{ponteiro.dado}\n\u2193\n"
            ponteiro=ponteiro.proximo
        frase+=f"{None}"
        return frase
