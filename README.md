# Algoritmo A* (A Estrela)

Este trabalho foi desenvolvido para a disciplina de Inteligência Artificial.

## Alunos

- [Leonardo Antunes Gonçalves](https://github.com/LeskeLense)
- [Cauã Nascimento Machado De Paula](https://github.com/CauaDePaula)
- [Cristiano Mafra Junior](https://github.com/CristianoMafraJunior)

## Explicação Teórica

O **Algoritmo A\*** (lê-se A-Estrela) é um algoritmo de busca em grafos que utiliza funções heurísticas. É amplamente utilizado em problemas de busca, devido à sua eficiência. O objetivo principal do algoritmo é encontrar o caminho mais curto entre dois pontos em um grafo.

O custo total de um nó é dado pela soma de duas funções:
- g(x): O custo real do nó inicial até o nó atual.
- h(x): A função heurística que estima o custo do nó atual até o nó de destino.

Portanto, a função de custo total (f(x)) é dada por:
f(x) = g(x) + h(x)

O Algoritmo A\* utiliza essa função de custo para escolher os próximos nós a serem explorados na busca pelo caminho mais curto.
