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

# Criação de um grafo dirigido utilizando um comando da biblioteca
G = nx.DiGraph()


#Criação dos nós, cada um representa um cruzamento, cada nó é identificado por algum rotulo unico
# Lista de cruzamentos (nós)
# Lista de cruzamentos (nós) e suas informações adicionais
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

# nó de origem, nó de destino, peso/segundos respectivamente
ruas = [
    ('0', '1', 5),
    ('1', '2', 10),
    ('2', '3', 7),
    ('3', '0', 8),
    ('0', '2', 12),
    ('1', '4', 15),
    ('4', '5', 10),
    ('5', '6', 5),
    ('6', '3', 20),
    ('2', '5', 14),
    ('4', '6', 8)
]

# Adicionando arestas ao grafo utilizando um comando da bilioteca 
G.add_weighted_edges_from(ruas)


# Verificação dos Caminhos Mínimos 
#O objetivo dessa verificação é assegurar que cada aresta 
#direta entre dois nós no grafo tem um peso que corresponde ao
#caminho mais curto possível entre esses nós, de acordo com o 
#algoritmo de Dijkstra

#Inicialização da Verificação:
is_minimal = True
#Iniciamos assumindo que o grafo está em caminho mínimo (is_minimal = True)
for u, v, weight in G.edges(data='weight'):
#Iteramos sobre todas as arestas do grafo. Para cada aresta, u é o nó de origem, 
#v é o nó de destino, e weight é o peso da aresta.
    shortest_path_length = nx.dijkstra_path_length(G, u, v)
#Calculamos o comprimento do caminho mínimo entre u e v usando o algoritmo de Dijkstra com 
#a função nx.dijkstra_path_length. Esta função retorna o comprimento do caminho mais curto entre u e v no grafo G.
    if weight != shortest_path_length:
        is_minimal = False
        break
#Comparamos o peso da aresta (weight) com o comprimento do caminho mínimo (shortest_path_length). 
#Se eles não são iguais, isso significa que o peso da aresta não representa o caminho mais curto possível entre u e v. Nesse caso, 
#definimos is_minimal como False e saímos do loop (break).
print("O grafo está em caminho mínimo?", is_minimal)

# variavel de Layout do grafo para uma visualização mais clara utilizando a biblioteca matplotlib.pyplo
# nx.spring_layout(G) gera um layout onde as posições dos nós são calculadas com base em um algoritmo de força.
layout = nx.spring_layout(G)



# essa variavel da biblioteca desenha os nós e as arestas do grafo.
# G é o grafo que queremos desenhar, layout é o nome das posições dos nós no gráfico.
# with_labels=True: Exibe os rótulos dos nós (nomes dos cruzamentos) no gráfico.
# node_size=700: Define o tamanho dos nós. Um valor maior resulta em nós maiores.
# node_color='lightblue': Define a cor dos nós. Aqui, os nós são coloridos em azul claro.
# font_size=15: Define o tamanho da fonte dos rótulos dos nós.
# font_color='black': Define a cor da fonte dos rótulos dos nós.
plt.figure(figsize=(12, 8))
nx.draw(G, layout, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_color='black')

# G: O grafo cujas arestas queremos rotular.
# layout: As posições dos nós no gráfico, devem ser as mesmas 
#utilizadas em nx.draw() para garantir que os rótulos das arestas sejam desenhados nos lugares corretos.
# edge_labels=labels: Um dicionário de rótulos para as arestas. O dicionário labels é criado pelo comando nx.get_edge_attributes(G, 'weight'),
#que retorna um dicionário onde as chaves são tuplas representando as arestas e os valores são os pesos dessas arestas.


#Adicionando rótulos com informações dos nós
node_labels = {node: f"{data['nome']}\nVerde: {data['tempo_verde']}s\nAmarelo: {data['tempo_amarelo']}s\nVermelho: {data['tempo_vermelho']}s\nVeículos:\nManhã: {data['numero_veiculos']['manha']}\nTarde: {data['numero_veiculos']['tarde']}\nNoite: {data['numero_veiculos']['noite']}" for node, data in G.nodes(data=True)}
nx.draw_networkx_labels(G, layout, labels=node_labels, font_size=10, font_color='darkblue')

# Título do gráfico
plt.title("Rede de Tráfego")
#comando para mostrar o grafo
plt.show()



