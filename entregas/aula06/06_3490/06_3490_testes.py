import unittest as test
import importlib

mod_pilha= importlib.import_module("06_3490_pilha_encadeada")
mod_fila= importlib.import_module("06_3490_fila_encadeada")
PilhaEncadeada=mod_pilha.PilhaEncadeada
FilaEncadeada=mod_fila.FilaEncadeada

class Teste_da_PilhaEncadeada(test.TestCase):
    def setUp(self):
        """Definimos o estado inicial do objeto de teste para cada uma das testagens da classe."""
        self.pilha=PilhaEncadeada()

    def test_ordem_LIFO(self):  #vamos testar se a ordem LIFO é obedecida
        """Testa-se se a ordem LIFO é obedecida no cenário de remoção pela nossa classe PilhaEncadeada."""
        pila=self.pilha
        pila.push(10)
        pila.push(20)
        pila.push(30)

        resultado_1=pila.pop()
        resultado_2=pila.pop()
        resultado_3=pila.pop()

        self.assertEqual(resultado_1, 30)
        self.assertEqual(resultado_2, 20)
        self.assertEqual(resultado_3, 10)

    def test_pop_e_topo_pilha_vazia(self):
        """Testa-se o que ocorre ao usarmos as funções pop e topo, em uma pilha vazia."""
        pill=self.pilha

        with self.assertRaises(IndexError):
            pill.pop()
        with self.assertRaises(IndexError):
            pill.topo()

    def test_coerência_do_len(self):
        """Testa-se a coerência de len após inserções e remoções."""
        pilas=self.pilha
        pilas.push(10)
        pilas.push(20)
        pilas.push(30)
        result_1=len(pilas)

        pilas.pop()
        result_2=len(pilas)

        pilas.pop()
        result_3=len(pilas)

        pilas.pop()
        result_4=len(pilas)

        self.assertEqual(result_1, 3)
        self.assertEqual(result_2, 2)
        self.assertEqual(result_3, 1)
        self.assertEqual(result_4, 0)

    def test_alternancia_de_operaçoes(self):
        """Valida o comportamento ao alternar empilhar e desempilhar."""
        pils=self.pilha

        pils.push(10)
        pils.push(20)
        pils.push(30)

        self.assertEqual(pils.pop(), 30)
#aqui a pilha esta no formato 10 -> 20
        pils.push(19)
        self.assertEqual(pils.topo(), 19)
        self.assertEqual(len(pils), 3)

    def test_arm_itens_dist(self):
        """Verifica se o armazenamento de itens de tipos diferentes está correto."""
        piala=self.pilha

        piala.push("Item do topo 01")
        resultado_01=type(piala.topo())

        piala.push(True)
        resultado_02=type(piala.topo())

        piala.push(10)
        resultado_03=type(piala.topo())

        piala.push(None)
        resultado_04=type(piala.topo())

        piala.push("10")
        resultado_05=type(piala.topo())

        self.assertEqual(resultado_01, str)
        self.assertEqual(resultado_02, bool)
        self.assertEqual(resultado_03, int)
        self.assertEqual(resultado_04, type(None))
        self.assertEqual(resultado_05, str)

class Teste_da_Fila_Encadeada(test.TestCase):
    def setUp(self):
        """Definimos o estado inicial do objeto de teste para cada uma das testagens da classe."""
        self.filsa=FilaEncadeada()

    def test_ordem_FIFO(self):
        """Testa-se a ordem First-in First-out da estrutura de dados FilaEncadeada."""
        filla=self.filsa
        filla.enfileirar(10)
        filla.enfileirar(20)
        filla.enfileirar(30)

        resultado_i1=filla.desenfileirar()
        resultado_i2=filla.desenfileirar()
        resultado_i3=filla.desenfileirar()

        self.assertEqual(resultado_i1, 10)
        self.assertEqual(resultado_i2, 20)
        self.assertEqual(resultado_i3, 30)

    def test_intercalar_operacoes(self):
        """Analisa-se o resultado da intercalação de enfileirar e desenfileirar."""
        fills=self.filsa

        fills.enfileirar(10)
        fills.enfileirar(20)
        fills.enfileirar(30)

        fills.desenfileirar()

        fills.enfileirar(40)
        fills.enfileirar("último item posto")

        fills.desenfileirar()
        fills.desenfileirar()

        results=fills.frente()

        self.assertEqual(results, 40)

    def test_uso_de_msm_instan(self):
        """Verifico se a fila é reutilizável em uma mesma instância."""
        fils=self.filsa

        fils.enfileirar("item 1")
        fils.enfileirar("item 2")

        fils.desenfileirar() #removo a string "item 1"

        fils.enfileirar("item 3")

        fils.desenfileirar()
        fils.desenfileirar()
        #adicionamos 3 itens e removemos 3 itens, logo, a fila está vazia

        teste_de_vazio=fils.esta_vazia()

        result_tamanh=len(fils)
        with self.assertRaises(IndexError):
            fils.frente()
        with self.assertRaises(IndexError):
            fils.desenfileirar()

        fils.enfileirar(10**2)
        fils.enfileirar(90)
        fils.enfileirar("IMPA-Tech")
        frente1=fils.frente()
        result2=fils.desenfileirar()
        resultfront=fils.frente()

        self.assertTrue(teste_de_vazio)
        self.assertEqual(result_tamanh, 0)
        self.assertEqual(frente1, 100)
        self.assertEqual(result2, 100)
        self.assertEqual(resultfront, 90)

    def test_desenfileirar_e_frente_pilha_vazia(self):
        """Testa-se o que ocorre ao usarmos as funções frente e desenfileirar, em uma fila vazia."""
        filha=self.filsa

        with self.assertRaises(IndexError):
            filha.desenfileirar()
        with self.assertRaises(IndexError):
            filha.frente()

    def test_coerencia_len(self):
        """Verifica-se a coerência do método len com alternância dos métodos enfileirar e desenfileirar."""
        filas=self.filsa
        filas.enfileirar(10)
        filas.enfileirar(20)
        filas.enfileirar(30)
        result_1=len(filas)

        filas.desenfileirar()
        result_2=len(filas)

        filas.desenfileirar()
        result_3=len(filas)

        filas.desenfileirar()
        result_4=len(filas)

        self.assertEqual(result_1, 3)
        self.assertEqual(result_2, 2)
        self.assertEqual(result_3, 1)
        self.assertEqual(result_4, 0)

if __name__ == '__main__':
    test.main()
