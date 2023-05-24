# Explicação do problema                                                                                      

Existe uma operação Troca(A, B): um elemento qualquer do vetor A recebe um valor de um elemento qualquer do vetor B. 

Além disso, temos um inteiro K que indica a maior quantidade possível de trocas que podem ser feitas. A operação Somatório(X) indica a soma de todos os valores de um vetor X.

Sendo assim, dados dois vetores A e B, qual é o maior valor possível de Somatório(A) com, no máximo, K trocas?

## Dados e regras do problema                                                                                 

* Trocas podem acontecer no mínimo 0 vezes e no máximo K vezes. 
* Os valores de cada vetor são números Naturais (i.e., todos os inteiros cujo valor é maior ou igual a 1).                                                                                 
  ​                                                                                                            
## Explicação da solução                                                                                      

A estratégia gulosa que escolhemos foi: troque o menor número de A pelo maior número de B. 

Para tanto, ordenamos A de maneira crescente e B de maneira decrescente. Sendo assim, o menor valor de A e o maior de B sempre estarão na primeira posição de seus respectivos vetores. Essas duas ordenações tem complexidade O(N * log N). 

Após a troca, reordene os vetores da mesma forma. Como eles estão quase ordenados (ou seja, mais próximo do melhor caso), a complexidade tende a O(N).

Faremos essas operações enquanto temos trocas disponíveis e enquanto o menor valor de A é, ainda, menor do que o maior valor de B.

Por fim, devolveremos o Somatório(A).
