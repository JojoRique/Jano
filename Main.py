# Passo 1: Definição do Escopo e Objetivos
# Objetivos:

# Minimizar o tempo de espera dos veículos nos cruzamentos.
# Reduzir congestionamentos.
# Melhorar a eficiência do sistema de tráfego.

#Comando e bibliotecas a serem usadas:

# Vamos instalar as bibliotecas essenciais que utilizaremos ao longo do projeto. 
# Isso inclui numpy para manipulação de dados numéricos, pandas para análise de dados,
# networkx para manipulação de grafos, e matplotlib para visualização.
# pip install numpy pandas networkx matplotlib
# 
#importando as bibliotecas necessárias:
# Copiar código
# import numpy as np
# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt

# abaixo estamos importando as bibliotecas a serem utilizadas, import *nome da biblioteca* as *Apelido* (normalmente damos certo apelidos por convenção)

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#representação de uma rede de tráfego com grafos, cada nó representa um cruzamento e cada aresta representa uma rua
#aqui usaremos a biblioteca de grafos networkx
#criação de uma variavel que será o grafo dirigo, por que grafo dirigido? pois ele permite simular fluxo de veículos em ruas e cruzamentos em direções especificas
G = nx.DiGraph()

#Criação dos nós, cada um representa um cruzamento, cada nó é identificado por algum rotulo unico
# Lista de cruzamentos (nós)
cruzamentos_info = {
    '0': {'nome': 'Cruzamento 0', 'tempo_verde': 30, 'tempo_amarelo': 5, 'tempo_vermelho': 25, 'numero_veiculos': {'manha': 20, 'tarde': 30, 'noite': 15}},
    '1': {'nome': 'Cruzamento 1', 'tempo_verde': 35, 'tempo_amarelo': 5, 'tempo_vermelho': 20, 'numero_veiculos': {'manha': 25, 'tarde': 35, 'noite': 20}},
    '2': {'nome': 'Cruzamento 2', 'tempo_verde': 25, 'tempo_amarelo': 5, 'tempo_vermelho': 30, 'numero_veiculos': {'manha': 30, 'tarde': 40, 'noite': 25}},
    '3': {'nome': 'Cruzamento 3', 'tempo_verde': 40, 'tempo_amarelo': 5, 'tempo_vermelho': 15, 'numero_veiculos': {'manha': 35, 'tarde': 45, 'noite': 30}},
    '4': {'nome': 'Cruzamento 4', 'tempo_verde': 20, 'tempo_amarelo': 5, 'tempo_vermelho': 35, 'numero_veiculos': {'manha': 15, 'tarde': 25, 'noite': 10}},
    '5': {'nome': 'Cruzamento 5', 'tempo_verde': 50, 'tempo_amarelo': 5, 'tempo_vermelho': 10, 'numero_veiculos': {'manha': 40, 'tarde': 50, 'noite': 35}},
    '6': {'nome': 'Cruzamento 6', 'tempo_verde': 45, 'tempo_amarelo': 5, 'tempo_vermelho': 20, 'numero_veiculos': {'manha': 50, 'tarde': 60, 'noite': 45}}
}


# Adicionando nós ao grafo utilizando um comando da bilioteca 
for cruzamento, info in cruzamentos_info.items():
    G.add_node(cruzamento, **info)
#As arestas representam as ruas entre os cruzamentos, os pesos são os segundos das arestas
# Lista de arestas com tempos de viagem em segundos

# nó de origem, nó de destino
# Lista de arestas, com pesos definidos aleatoriamente
ruas = [
    ('0', '1'),
    ('1', '2'),
    ('2', '3'),
    ('3', '0'),
    ('0', '2'),
    ('1', '4'),
    ('4', '5'),
    ('5', '6'),
    ('6', '3'),
    ('2', '5'),
    ('4', '6')
]

# Função para calcular o tempo de viagem ajustado pelo semáforo
def calcular_tempo_viagem(origem, destino, tempo_basico):
#origem: O nó de origem (cruzamento de partida).
#destino: O nó de destino (cruzamento de chegada). Note que, nesta implementação específica, destino não é utilizado.
#tempo_basico: O tempo básico de viagem entre a origem e o destino (sem considerar semáforos).  

    tempo_verde = cruzamentos_info[origem]['tempo_verde']
    tempo_amarelo = cruzamentos_info[origem]['tempo_amarelo']
    tempo_vermelho = cruzamentos_info[origem]['tempo_vermelho']
#tempo_verde, tempo_amarelo e tempo_vermelho: 
#Extrai os tempos de sinal verde, amarelo e vermelho 
#para o nó de origem a partir do dicionário cruzamentos_info.
    ciclo_semaforo = tempo_verde + tempo_amarelo + tempo_vermelho
#ciclo_semaforo: Calcula o ciclo completo do semáforo somando os tempos de sinal verde,
# amarelo e vermelho. Esse valor representa o tempo total para um ciclo completo de semáforo.
    tempo_espera = tempo_vermelho  # Supondo que o tempo de espera é o tempo do sinal vermelho
    
    tempo_total = tempo_basico + tempo_espera
    return tempo_total

# Adicionando arestas ao grafo com pesos ajustados pelos semáforos
for u, v in ruas:
#ruas é uma lista de tuplas representando as ruas (arestas) do grafo.
#Cada tupla (u, v) representa uma aresta do nó u (origem) ao nó v (destino)
#A iteração percorre todas as arestas definidas em ruas.

    tempo_basico = np.random.randint(1, 20)  # Tempo básico de viagem
#tempo_basico: Um tempo de viagem aleatório entre 1 e 19 segundos é gerado usando np.random.randint(1, 20).
#Este valor representa o tempo de viagem sem considerar a espera no semáforo.
    tempo_ajustado = calcular_tempo_viagem(u, v, tempo_basico)
#calcular_tempo_viagem(u, v, tempo_basico): A função calcular_tempo_viagem é chamada com os parâmetros u (origem), v (destino), e tempo_basico.
#A função retorna o tempo_ajustado, que é o tempo_basico acrescido do tempo de espera no semáforo do nó de origem u.
    G.add_edge(u, v, weight=tempo_ajustado)
#G.add_edge(u, v, weight=tempo_ajustado): Adiciona a aresta do nó u ao nó v no grafo G, com um peso (atributo weight) igual ao tempo_ajustado.
#O peso da aresta representa o tempo de viagem ajustado considerando o impacto dos semáforos.

# Definindo o nó de origem e o nó de destino
source = '0'
target = '6'

# Encontrar o caminho mínimo usando o algoritmo de Dijkstra
path = nx.dijkstra_path(G, source, target)
path_length = nx.dijkstra_path_length(G, source, target)

# Visualização do grafo
plt.figure(figsize=(12, 8))
layout = nx.spring_layout(G)

# Desenhar o grafo com os pesos das arestas
nx.draw(G, layout, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_color='black')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, layout, edge_labels=edge_labels, font_color='red', font_size=12)

# Destacar o caminho mínimo no grafo
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, layout, edgelist=path_edges, edge_color='green', width=2)

# Adicionar rótulos com informações dos nós
node_labels = {node: f"{data['nome']}\nVerde: {data['tempo_verde']}s\nAmarelo: {data['tempo_amarelo']}s\nVermelho: {data['tempo_vermelho']}s\nVeículos:\nManhã: {data['numero_veiculos']['manha']}\nTarde: {data['numero_veiculos']['tarde']}\nNoite: {data['numero_veiculos']['noite']}" for node, data in G.nodes(data=True)}
nx.draw_networkx_labels(G, layout, labels=node_labels, font_size=10, font_color='darkblue')

# Título do gráfico
plt.title(f"Rede de Tráfego\nCaminho Mínimo de {source} a {target}: {path} (Comprimento: {path_length})")
plt.show()
