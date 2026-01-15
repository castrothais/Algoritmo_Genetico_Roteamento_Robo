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

- Para cada pai a ser selecionado, são sorteados 10 indivíduos da população atual
- O indivíduo com menor custo é escolhido entre esses 10 e selecionado como pai
- Esse processo se repete até que sejam selecionados 10 pais, podendo ocorrer repetição de indivíduos, uma vez que os torneios são realizados de forma independente

### 🔹 Operador de Crossover

- **Crossover Multiponto (2 pontos de corte)**
- O cromossomo do filho é formado pela combinação de três segmentos:
  - Trecho inicial é do primeiro pai
  - Segundo trecho é do segundo pai
  - Último trecho é do primeiro pai
- Durante o crossover, são realizadas validações para garantir que o robô não ultrapasse os limites da grade
- Caso o objetivo seja alcançado durante a construção do cromossomo, o processo é interrompido antecipadamente
- Caso o objetivo não seja alcançado, o caminho é completado aleatoriamente

### 🔹 Operador de Mutação

- **Mutação:**
Mutação **híbrida** com dois tipos principais:

1. **Alteração simples** (75% de chance)  
   - Escolhe aleatoriamente uma posição no cromossomo  
   - Substitui o movimento atual por outro movimento diferente (entre os 4 possíveis)

2. **Troca (swap)** (25% de chance)  
   - Seleciona duas posições diferentes no caminho  
   - Troca os movimentos entre essas posições

Após a mutação:

- Remove movimentos que levariam o robô para fora da grade
- Se necessário, completa o caminho até o objetivo com movimentos aleatórios válidos
- Durante o reparo, evita movimentos que levem diretamente a obstáculos

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
