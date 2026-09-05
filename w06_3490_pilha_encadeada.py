class No:
        def __init__(self, dado):
            self.dado = dado
            self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.top = None
        self.tamanho = 0
    def push(self, dado):
        new=No(dado)
        new.proximo=self.top
        self.top=new
        self.tamanho+=1
    def pop(self):
        if self.top==None:
            raise IndexError("Objeto vazio")
        dado_removido=self.top.dado
        self.top=self.top.proximo
        self.tamanho-=1
        return dado_removido
    def topo(self):
        if self.top==None:
            raise IndexError("Objeto vazio")
        return self.top.dado
    def esta_vazia(self):
        if self.top is None:
            return True
        else:
            return False
    def __len__(self):
        return self.tamanho
    def __repr__(self):
        ponteiro=self.top  #pra onde o meu ponteiro aponta atualmente (inicialmente no topo)
        frase=f""
        while ponteiro is not None:
            frase+=f"{ponteiro.dado}\n\u2193\n"
            ponteiro=ponteiro.proximo
        frase+=f"{None}"
        return frase