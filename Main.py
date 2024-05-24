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
cruzamentos = ['A', 'B', 'C', 'D']

# Adicionando nós ao grafo utilizando um comando da bilioteca 
G.add_nodes_from(cruzamentos)

#As arestas representam as ruas entre os cruzamentos, os pesos são os segundos das arestas
# Lista de arestas com tempos de viagem em segundos

# nó de origem, nó de destino, peso/segundos respectivamente
ruas = [
    ('A', 'B', 5),
    ('B', 'C', 10),
    ('C', 'D', 7),
    ('D', 'A', 8),
    ('A', 'C', 12)
]

# Adicionando arestas ao grafo utilizando um comando da bilioteca 
G.add_weighted_edges_from(ruas)

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

nx.draw(G, layout, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_color='black')

# G: O grafo cujas arestas queremos rotular.
# layout: As posições dos nós no gráfico, devem ser as mesmas 
#utilizadas em nx.draw() para garantir que os rótulos das arestas sejam desenhados nos lugares corretos.
# edge_labels=labels: Um dicionário de rótulos para as arestas. O dicionário labels é criado pelo comando nx.get_edge_attributes(G, 'weight'),
#que retorna um dicionário onde as chaves são tuplas representando as arestas e os valores são os pesos dessas arestas.

# Adicionando rótulos com os pesos das arestas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)

# Título do gráfico
plt.title("Rede de Tráfego")
#comando para mostrar o grafo
plt.show()



