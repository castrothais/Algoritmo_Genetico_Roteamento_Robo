<!-- markdownlint-disable-next-line MD033 -->
<h1 align="center"> 🤖 Algoritmo Genético para Roteamento de Robô </h1>

Este projeto implementa um **Algoritmo Genético (AG)** para resolver um problema de **roteamento de robô em ambiente bidimensional com obstáculos**, buscando um caminho de menor custo entre um ponto inicial e um ponto objetivo.

O robô se move em uma grade `N x N`, podendo realizar movimentos para cima, baixo, esquerda e direita, evitando obstáculos distribuídos aleatoriamente no ambiente.

## 📌 Descrição do Problema

- Ambiente bidimensional com obstáculos
- Ponto inicial fixo e ponto objetivo definido
- Cada solução representa uma sequência de movimentos
- O custo da solução considera:
  - Comprimento do caminho
  - Penalização por colisões com obstáculos

## ⚙️ Configuração do Algoritmo Genético

### 🔹 Representação do Cromossomo

- Cada cromossomo é uma **lista de movimentos**
- Movimentos possíveis:
  - `1` → Cima
  - `2` → Direita
  - `3` → Baixo
  - `4` → Esquerda

### 🔹 Parâmetros do AG

| Parâmetro | Valor |
| --------- | ------- |
| Tamanho da população | 100 |
| Total de pais por geração | 10 |
| Critério de seleção | Torneio |
| Proporção de crossover | 60% |
| Proporção de mutação | 30% |
| Penalização por obstáculo | 50 |
| Critério de parada | 200 gerações sem melhora |

---

### 🔹 Seleção dos Pais

- Para cada pai a ser selecionao, são sorteados 10 da população atual
- O indivíduo com menor custo é escolhido entre esses 10. Em seguida, é selecionado como pai
- Esse processo se repete até que sejam escolhidos 10 pais distintos

### 🔹 Operador de Crossover

- **Crossover Multiponto (2 pontos de corte)**
- O cromossomo do filho é formado pela combinação de três segmentos:
  - Trecho inicial é do primeiro pai
  - Segundo trecho é do segundo pai
  - Último trecho é do primeiro pai
- Caso o objetivo não seja alcançado, o caminho é completado aleatoriamente

### 🔹 Operador de Mutação

- **Mutação:** EM ANDAMENTO

## 🛑 Critério de Parada

O algoritmo é interrompido quando:

- Não ocorre melhoria da melhor solução encontrada após **200 gerações consecutivas**

## 📊 Visualização

O projeto inclui a visualização gráfica:

- Obstáculos (amarelo)
- Caminho do robô (azul)
- Colisões com obstáculos (vermelho)

## 🧪 Tecnologias Utilizadas

- Python 3
- Biblioteca `random`
- Biblioteca `matplotlib`

## ✍️ Autoria

Projeto desenvolvido por **Thais Sampaio e Hudson Werneck**  
Disciplina: Otimização Combinatória
