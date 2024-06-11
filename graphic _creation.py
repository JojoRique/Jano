import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Função para calcular o tempo de viagem ajustado pelo semáforo


def calcular_tempo_viagem(origem, destino, tempo_basico, cruzamentos_info):
    tempo_verde = cruzamentos_info[origem]['tempo_verde']
    tempo_amarelo = cruzamentos_info[origem]['tempo_amarelo']
    tempo_vermelho = cruzamentos_info[origem]['tempo_vermelho']

    ciclo_semaforo = tempo_verde + tempo_amarelo + tempo_vermelho
    # Supondo que o tempo de espera é o tempo do sinal vermelho
    tempo_espera = tempo_vermelho

    tempo_total = tempo_basico + tempo_espera
    return tempo_total

# Função para criar o grafo com tempos de viagem ajustados


def criar_grafo(cruzamentos_info, ruas):
    G = nx.DiGraph()
    for cruzamento, info in cruzamentos_info.items():
        G.add_node(cruzamento, **info)

    for u, v in ruas:
        tempo_basico = np.random.randint(1, 20)  # Tempo básico de viagem
        tempo_ajustado = calcular_tempo_viagem(
            u, v, tempo_basico, cruzamentos_info)
        G.add_edge(u, v, weight=tempo_ajustado)

    return G


# Definir cruzamentos e ruas
cruzamentos_info = {
    '0': {'nome': 'Cruzamento 0', 'tempo_verde': 30, 'tempo_amarelo': 5, 'tempo_vermelho': 25},
    '1': {'nome': 'Cruzamento 1', 'tempo_verde': 35, 'tempo_amarelo': 5, 'tempo_vermelho': 20},
    '2': {'nome': 'Cruzamento 2', 'tempo_verde': 25, 'tempo_amarelo': 5, 'tempo_vermelho': 30},
    '3': {'nome': 'Cruzamento 3', 'tempo_verde': 40, 'tempo_amarelo': 5, 'tempo_vermelho': 15},
    '4': {'nome': 'Cruzamento 4', 'tempo_verde': 20, 'tempo_amarelo': 5, 'tempo_vermelho': 35},
    '5': {'nome': 'Cruzamento 5', 'tempo_verde': 50, 'tempo_amarelo': 5, 'tempo_vermelho': 10},
    '6': {'nome': 'Cruzamento 6', 'tempo_verde': 45, 'tempo_amarelo': 5, 'tempo_vermelho': 20}
}

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

# Simular vários cenários
tempos_viagem = []

for _ in range(10):  # Simular 10 cenários diferentes
    G = criar_grafo(cruzamentos_info, ruas)
    source = '0'
    target = '6'
    path_length = nx.dijkstra_path_length(G, source, target)
    tempos_viagem.append(path_length)

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(tempos_viagem, marker='o', linestyle='-', color='b')
plt.xlabel('Cenário')
plt.ylabel('Tempo de Viagem (s)')
plt.title('Comparação de Tempos de Viagem em Diferentes Cenários')
plt.grid(True)
plt.show()
