# 📘 Tarefa: Algoritmos de Grafos e Caminhos Mínimos

## 🎯 Objective

Aplicar estruturas de dados e algoritmos avançados para resolver problemas de caminho em grafos. Você irá implementar BFS e Dijkstra, comparar resultados e analisar complexidade em cenários diferentes.

## 📝 Tasks

### 🛠️ Modelar o Grafo e Encontrar Caminho com BFS

#### Descrição
Implemente a representação de um grafo não direcionado e não ponderado com lista de adjacência. Depois, use BFS para encontrar o menor caminho em número de arestas entre dois nós.

#### Requisitos
O programa completo deve:

- Representar o grafo em uma estrutura de dados clara e reutilizável
- Implementar `bfs_shortest_path(graph, start, end)` retornando a lista de nós do caminho
- Retornar lista vazia quando não houver caminho entre `start` e `end`
- Demonstrar o algoritmo com ao menos dois casos de teste simples


### 🛠️ Implementar Dijkstra para Grafos Ponderados

#### Descrição
Adapte a representação para incluir pesos nas arestas e implemente o algoritmo de Dijkstra para encontrar o caminho de menor custo total.

#### Requisitos
O programa completo deve:

- Implementar `dijkstra_shortest_path(graph, start, end)` usando fila de prioridade (`heapq`)
- Retornar uma tupla com `(distancia_total, caminho)`
- Validar que todos os pesos são não negativos antes de executar Dijkstra
- Demonstrar o resultado em um grafo ponderado com pelo menos 6 nós


### 🛠️ Comparar Estratégias e Analisar Complexidade

#### Descrição
Compare BFS e Dijkstra em grafos apropriados e explique quando cada abordagem deve ser usada. Produza saídas que permitam justificar a escolha do algoritmo.

#### Requisitos
O programa completo deve:

- Executar BFS e Dijkstra em cenários equivalentes e exibir resultados lado a lado
- Informar quando o menor caminho por arestas difere do menor caminho por custo
- Exibir uma análise breve de complexidade assintótica de cada algoritmo
- Incluir pelo menos um caso em que Dijkstra encontra rota com mais arestas, porém menor custo total
