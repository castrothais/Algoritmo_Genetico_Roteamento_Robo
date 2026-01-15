'''

Projeto Algoritmo Genético
Alunos: Hudson Werneck e Thaís de Castro

'''

#Problema de Roteamento de Robo
import random
import matplotlib.pyplot as plt
import time

tempo_inicio = time.time()

# Ambiente
random.seed(3)
N = 30
Obs = N*10
inicio = [0, 0]
pen = 50
objetivo = [N-1, N-1]

obstaculos = set()
while len(obstaculos) < Obs:
    x = random.randint(0, N-1)
    y = random.randint(0, N-1)
    if (x, y) != inicio and (x, y) != objetivo:
        obstaculos.add((x, y))
obstaculos = list(obstaculos)
obstaculos.sort()
random.seed()

movimentos = {
    1: (0, 1),    # Cima
    2: (1, 0),    # Direita
    3: (0, -1),   # Baixo
    4: (-1, 0)    # Esquerda
}

def aptidao(Sol):
    passo = inicio[:]
    tot = 0
    for i in range(len(Sol)):
        mov = Sol[i]
        cx = movimentos[mov][0]
        cy = movimentos[mov][1]
        passo[0] += cx
        passo[1] += cy
        if tuple(passo) in obstaculos:
            tot += 1
    custo = len(Sol) + tot * pen
    return custo

def imprimeGrafico(Sol):
    x = []
    y = []
    for i in range(len(obstaculos)):
        x.append(obstaculos[i][0])
        y.append(obstaculos[i][1])
    plt.scatter(x, y, color='y')
    x = []
    y = []
    x.append(inicio[0])
    y.append(inicio[1])
    plt.scatter(x, y, color='c')
   
    x = []
    y = []
    w = []
    z = []
    a = []
    b = []
    passo=inicio[:]
    for i in range(len(Sol)):
        mov = Sol[i]
        cx = movimentos[mov][0]
        cy = movimentos[mov][1]
        passo[0] += cx
        passo[1] += cy
        x.append(passo[0])
        y.append(passo[1])
        if tuple(passo) in obstaculos:
            w.append(passo[0])
            z.append(passo[1])
        if passo == objetivo:
            a.append(passo[0])
            b.append(passo[1])
    plt.scatter(x, y, color='b')
    plt.scatter(w, z, color='r')
    plt.scatter(a, b, color='g')

    plt.show()
    return()

def crossover(p1, p2, mov):
    lim = min(len(p1), len(p2))
    corte1 = random.randint(5, lim - 15)
    corte2 = random.randint(corte1 + 5, lim - 10)
    filho = []
    passo = inicio[:]
    
    for i in range(corte1):
        mv = p1[i]
        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]
        if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
            filho.append(mv)
            passo = npasso[:]
        if passo == objetivo:
            return filho
   
    for i in range(corte1, corte2):
        mv = p2[i]
        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]
        if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
            filho.append(mv)
            passo = npasso[:]
        if passo == objetivo:
            return filho
   
    for i in range(corte2, len(p1)):
        mv = p1[i]
        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]
        if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
            filho.append(mv)
            passo = npasso[:]
        if passo == objetivo:
            return filho
            
    while passo != objetivo:
        mv = random.randint(1, len(mov))
        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]
        if (0 <= npasso[0] < N and 0 <= npasso[1] < N):
            filho.append(mv)
            passo = npasso[:]
        if passo == objetivo:
            return filho

def mutacao(p1):
    caminho = p1[:]
    
    if len(caminho) < 3:
        idx = random.randint(0, len(caminho)-1)
        atual = caminho[idx]
        possiveis = [m for m in [1,2,3,4] if m != atual]
        caminho[idx] = random.choice(possiveis)
        return caminho
    
    if random.random() < 0.75:
        idx = random.randint(0, len(caminho)-1)
        atual = caminho[idx]
        possiveis = [m for m in [1,2,3,4] if m != atual]
        novo = random.choice(possiveis)
        caminho[idx] = novo
    else:
        i = random.randint(0, len(caminho)-1)
        j = random.randint(0, len(caminho)-1)
        while i == j:
            j = random.randint(0, len(caminho)-1)
        caminho[i], caminho[j] = caminho[j], caminho[i]
    
    caminho_limpo = []
    pos = inicio[:]
    for mv in caminho:
        novo_pos = [pos[0] + movimentos[mv][0], pos[1] + movimentos[mv][1]]
        if (0 <= novo_pos[0] < N and 0 <= novo_pos[1] < N):
            caminho_limpo.append(mv)
            pos = novo_pos
        if pos == objetivo:
            return caminho_limpo
    
    while pos != objetivo and len(caminho_limpo) < len(p1) * 2:
        possiveis = []
        for m in [1,2,3,4]:
            nx = pos[0] + movimentos[m][0]
            ny = pos[1] + movimentos[m][1]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in obstaculos:
                possiveis.append(m)
        
        if not possiveis:
            break
        
        mv = random.choice(possiveis)
        caminho_limpo.append(mv)
        pos[0] += movimentos[mv][0]
        pos[1] += movimentos[mv][1]
    
    return caminho_limpo

# Geração da população inicial
cxi = inicio[0]
cyi = inicio[1]
cxf = objetivo[0]
cyf = objetivo[1]
mov = []
if cxi < cxf:
    mov.append(2)
else:
    mov.append(4)
if cyi < cyf:
    mov.append(1)
else:
    mov.append(3)

tamPop = 100
cont = 0
Pop = []
custoBest = 999999

while cont < tamPop:
    cont += 1
    Sol = []
    passo = inicio[:]
    while passo != objetivo:
        mv = random.randint(1, len(mov))
        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]
        if npasso[0] <= cxf and npasso[1] <= cyf:
            Sol.append(mv)
            passo = npasso[:]
    custo = aptidao(Sol)
    Pop.append([custo, Sol])
    if custo < custoBest:
        Best = Sol[:]
        custoBest = custo

# Geração Populacional
ger = 0
totGer = 200
totPais = 10
txMut = 30
txCros = 60

def selecao_pais_torneio(pop, totPais):
    pais = []
    for i in range(totPais):
        torneio = random.sample(pop, 10)
        melhor = min(torneio, key=lambda x: x[0])
        pais.append(melhor)
    return pais

while ger <= totGer:
    ger += 1
    
    Pais = selecao_pais_torneio(Pop, totPais)
    Pop = Pais[:]
    
    cont = 0
    while cont < txCros:
        cont += 1
        p1 = random.randint(0, totPais-1)
        p2 = random.randint(0, totPais-1)
        while p1 == p2:
            p1 = random.randint(0, totPais-1)
        p1 = Pop[p1][1]
        p2 = Pop[p2][1]
        filho = crossover(p1, p2, mov)
        custo = aptidao(filho)
        Pop.append([custo, filho])
        if custo < custoBest:
            Best = filho[:]
            custoBest = custo
            ger = 0
            print('cros', custoBest)
           
    cont = 0
    while cont < txMut:
        cont += 1
        p1 = random.randint(0, totPais-1)
        p1 = Pop[p1][1]
        filho = mutacao(p1)
        custo = aptidao(filho)
        Pop.append([custo, filho])
        if custo < custoBest:
            Best = filho[:]
            custoBest = custo
            ger = 0
            print('mut', custoBest)
   
Pop.sort(key=lambda x: x[0])
Pop = Pop[:tamPop]

custo = aptidao(Best)
print('Custo da Best', custoBest)
imprimeGrafico(Best)

tempo_fim = time.time()
tempo_total = tempo_fim - tempo_inicio
print(f"Tempo de execução: {tempo_total:.2f} segundos")
