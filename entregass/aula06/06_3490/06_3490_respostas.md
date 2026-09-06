#Análise da Complexidade do método Desenfileirar

Para a implementação da classe FilaEncadeada alicerçada na classe PilhaEncadeada, é necessário
o uso da ideia de que a fila é composta por duas pilhas, uma para entrada dos elementos na fila
(pilha_de_entrada) e outra para controlar a ordem de saída dos dados da fila (pilha_de_saida).
Tendo visto isso, imagine o seguinte cenário:
——Temos "n" dados na pilha_de_entrada, mas na pilha_de_saida (que contém os dados, do topo para a 
base, na ordem de entrada na fila) temos "k" elementos. Veja que para desenfileirar, basta apenas
usar o método pop() da classe PilhaEncadeada de complexidade O(1). Perceba, ainda, que em momento
algum foi útil a informação que fazia menção a quantidade de itens na pilha_de_entrada.
Agora, visualize esta situação hipotética:
——Existem "n" valores na pilha_de_entrada, mas a pilha_de_saida está vazia. Observe que para removermos
o elemento mais antigo, devemos transferir todos os elementos da pilha_de_entrada para a pilha_de_saida.
Para tanto, deve-se realizar um laço para percorrermos os itens da pilha_de_entrada, usar o método pop()
neles em relação a pilha_de_entrada e efetuar o método push() na pilha_de_saida, para, dessa forma,
adicionar esse elemento removido na pilha_de_saida. Ou seja, levamos n passos para remover os itens e mais
n passos para adicionálos na segunda pilha (isto pois, os métodos pop() e push() possuem complexidade O(1)).
Nesse sentido, temos a complexidade de O(n), já que n+n=2*n, um tempo linear. No entanto, suponha que fizemos isso
e então removemos o item, é imediato que a Fila Encadeada terá tamanho n-1, mas se o método desenfileirar for chamado nas próximas n-1 vezes ele terá complexidade O(1) para remover e retornar cada um desses n-1 objetos. Em suma, nota-se que cada elemento é transferido da pilha de entrada para a de saída exatamente 1 única vez durante toda a sua existência na fila, o que auxilia na complexidade amortizada O(1) do método desenfileirar.