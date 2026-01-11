'''

Projeto Algoritmo Genético
Alunos: Hudson Werneck e Thaís de Castro

'''

#Problema de Roteamento de Robo
import random
import matplotlib.pyplot as plt

#Ambiente
random.seed(3)  #para gerar as mesmas instâncias a partir da mesma semente
N = 30
Obs = N*10
inicio = [0, 0]
pen = 50
objetivo = [N-1, N-1]
obstaculos = set() #gera os obstáculos sem repetição de coordenadas
while len(obstaculos) < Obs:
    x = random.randint(0, N-1)
    y = random.randint(0, N-1)
    if (x, y) != inicio and (x, y) != objetivo:
        obstaculos.add((x, y))
obstaculos = list(obstaculos) #transformação em lista para facilitar o uso de métodos
obstaculos.sort()
random.seed()

#Coordenadas dos movimentos possíveis: 1=Cima, 2=Direita, 3=Baixo, 4=Esquerda
movimentos = {
    1: (0, 1),   # Cima
    2: (1, 0),   # Direita
    3: (0, -1),  # Baixo
    4: (-1, 0)   # Esquerda
}

def aptidao(Sol):
    passo=inicio[:]
    tot=0
    for i in range(len(Sol)):
        mov=Sol[i]
        cx = movimentos[mov][0]
        cy = movimentos[mov][1]
        passo[0]+=cx
        passo[1]+=cy
        if tuple(passo) in obstaculos:
            tot+=1
    custo=len(Sol)+tot*pen
    return(custo)

def imprimeGrafico(Sol):
    #Imprime obstáculos
    x=[]
    y=[]
    for i in range(len(obstaculos)):
        x.append(obstaculos[i][0])
        y.append(obstaculos[i][1])
    plt.scatter(x, y, color='y')
    
    #Imprime a Solução
    x=[]
    y=[]
    w=[]
    z=[]
    passo=inicio[:]
    for i in range(len(Sol)):
        mov=Sol[i]
        cx = movimentos[mov][0]
        cy = movimentos[mov][1]
        passo[0]+=cx
        passo[1]+=cy
        x.append(passo[0])
        y.append(passo[1])
        if tuple(passo) in obstaculos:
            w.append(passo[0])
            z.append(passo[1])
    plt.scatter(x, y, color='b')
    plt.scatter(w, z, color='r')
        
    plt.show()
    return()

def crossover(p1, p2,mov):
    lim = min(len(p1), len(p2))
    if lim < 20:
        return p1[:]

    corte1 = random.randint(5, lim//2)
    corte2 = random.randint(corte1 + 1, lim - 5)

    filho = []
    passo = inicio[:]

    for i in range(lim):
        if i < corte1:
            mv = p1[i]
        elif i < corte2:
            mv = p2[i]
        else:
            mv = p1[i]

        npasso = passo[:]
        npasso[0] += movimentos[mv][0]
        npasso[1] += movimentos[mv][1]

        if (npasso[0] >= 0 and npasso[0] < N and
            npasso[1] >= 0 and npasso[1] < N):
            filho.append(mv)
            passo = npasso[:]

        if (passo[0] == objetivo[0] and passo[1] == objetivo[1]):
            return filho
        
    while (passo != objetivo):
        mv=random.randint(1, len(mov))
        npasso=passo[:]
        npasso[0]+=movimentos[mv][0]
        npasso[1]+=movimentos[mv][1]
        if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
            filho.append(mv)
            passo=npasso[:]
        if (npasso[0]==objetivo[0] and npasso[1]==objetivo[1]):
            return(filho)


def mutacao(p1):
    obs=[] #armazena a posição dentro dos movimentos realizados em que a solução cruza um obstáculo
    passo=inicio[:]
    for i in range(len(p1)):
        mv=p1[i]
        passo[0]+=movimentos[mv][0]
        passo[1]+=movimentos[mv][1]
        if tuple(passo) in obstaculos:
            obs.append([i, mv])
    if (len(obs)==0): #se não tiver obstáculos faz uma troca aleatória qualquer
       i=random.randint(0, len(p1)-1)
       mv=p1[i]
       obs.append([i, mv])
    sai=random.randint(0, len(obs)-1) #troca o movimento que colide em um obstáculo sorteado (sai) por outro sorteado (entra)
    entra=random.randint(1, 4)
    while (entra==obs[sai][1]):
        entra=random.randint(1, 4)
    p1[obs[sai][0]]=entra
    filho=[]
    passo=inicio[:]
    for i in range(len(p1)):
        npasso=passo[:]
        if (passo != objetivo):
            mv=p1[i]
            npasso[0]+=movimentos[p1[i]][0]
            npasso[1]+=movimentos[p1[i]][1]
            if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
                filho.append(mv)
                passo=npasso[:]
        if (npasso[0]==objetivo[0] and npasso[1]==objetivo[1]):
            return(filho)
    while (passo != objetivo):
        mv=random.randint(1, len(mov))
        npasso=passo[:]
        npasso[0]+=movimentos[mv][0]
        npasso[1]+=movimentos[mv][1]
        if (npasso[0]>=0 and npasso[0]<N and npasso[1]>=0 and npasso[1]<N):
            filho.append(mv)
            passo=npasso[:]
        if (npasso[0]==objetivo[0] and npasso[1]==objetivo[1]):
            return(filho)



#Geração da população inicial

cxi = inicio[0]
cyi = inicio[1]

cxf = objetivo[0]
cyf = objetivo[1]


mov=[]

if (cxi<cxf):
    mov.append(2)
else:
    mov.append(4)

if (cyi<cyf):
    mov.append(1)
else:
    mov.append(3)


tamPop=100
cont=0
Pop=[]
custoBest=999999

while (cont<tamPop):
    cont+=1
    Sol=[]
    passo=inicio[:]
    while (passo != objetivo):
        mv=random.randint(1, len(mov))
        npasso=passo[:]
        npasso[0]+=movimentos[mv][0]
        npasso[1]+=movimentos[mv][1]
        if (npasso[0]<=cxf and npasso[1]<=cyf):
            Sol.append(mv)
            passo=npasso[:]
            #print (passo)
    custo=aptidao(Sol)
    Pop.append([custo, Sol])
    if (custo<custoBest):
        Best=Sol[:]
        custoBest=custo

#Geração Populacional
ger=0
totGer=200
totPais=10
txMut=30
txCros=60

def selecao_pais_torneio(pop, k, tot_Pais):
    pais = []
    tamanho_grupo = 10

    for i in range(0, len(pop), tamanho_grupo):
        grupo = pop[i:i + tamanho_grupo]
        torneio = random.sample(grupo, 3)
        torneio.sort(key=lambda x: x[0]) # Como tem primeiro o custo e depois o caminho, coloquei para ordenar pelo custo
        pais.append(torneio[0])

    return pais
    
while (ger<=totGer):
    ger+=1
    tam_grupo = 10
    Pais = selecao_pais_torneio(Pop, 3, totPais)
    
    #Operador genético de Crossover
    cont=0
    while(cont<txCros):
        cont+=1
        p1_idx = random.randint(0, len(Pais)-1)
        p2_idx = random.randint(0, len(Pais)-1)
        while p2_idx == p1_idx:
            p2_idx = random.randint(0, len(Pais)-1)
        p1 = Pais[p1_idx][1]
        p2 = Pais[p2_idx][1]
        filho=crossover(p1,p2,mov)
        custo=aptidao(filho)
        Pop.append([custo, filho])
        if (custo<custoBest):
            Best=filho[:]
            custoBest=custo
            ger=0
            print('cros', custoBest)
            
    #Operador genético de Mutação
    cont=0
    while(cont<txMut):
        cont+=1
        p_idx = random.randint(0, len(Pais)-1)
        p1 = Pais[p_idx][1][:]
        filho=mutacao(p1)
        custo=aptidao(filho)
        Pop.append([custo, filho])
        if (custo<custoBest):
            Best=filho[:]
            custoBest=custo
            ger=0
            print('mut', custoBest)
    #print('Geração', ger)
    
Pop.sort(key=lambda x: x[0])
Pop = Pop[:tamPop]


custo=aptidao(Best)
print('Custo da Best', custoBest)
imprimeGrafico(Best)
