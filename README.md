# ProjetoFinal

Projeto final do aluno Giovanni Guarnieri Soares

O projeto consiste em dois códigos que resolvem equações diferenciais parciais, cada um com um método diferente.

Um dos métodos utilizados é o método de Relaxação. Ele percorre uma matriz quadrada de ordem n buscando fazer uma média entre os 4 elementos em volta de cada elemento percorrido, depois feito isso em toda matriz, passando por uma quantidade considerável de passos, é dada a solução para cada ponto.

A precisão do método  dada pela quantidade de elementos na matriz, quanto mais elementos mais fina é a grade e melhor é o sistema.

O outro método nos dá uma solução exata do sistema por um todo, em um só passo de "relaxação". A ideia é transformar cada elemento da matriz a ser relaxada em uma linha inteira de uma outra matriz e depois resolver o sistema de equações que aparece do método, utilizando o método de Gauss-Jordan. A matriz formada é da ordem n² e o código tem uma complexidade muito maior do que o anterior, então para tamanhos grandes (como n = 100) o código vai demorar muito mais pra finalizar do que o outro método.
