import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Dicionário de cores para cada tipo de ingrediente
tipo_cores = {
    'Carboidrato': 'green',
    'Proteína': 'blue',
    'Vegetal': 'orange',
    'Laticínio': 'purple',
    'Leguminosa': 'brown',
    'Gordura': 'pink',
    'Fruta': 'yellow',
    'Condimento': 'red'
}

# Carregar o arquivo CSV
file_path = 'receitas.csv'  # Substitua pelo caminho correto do arquivo
df = pd.read_csv(file_path, sep=";")

# Criar um grafo não direcionado
G = nx.Graph()

# Processar as receitas para adicionar os nós e arestas
for index, row in df.iterrows():
    ingredientes = row['ingredientes'].split(', ')
    tipos = row['tipos de ingredientes'].split(', ')
    
    # Adicionando nós com atributos (tipo de ingrediente)
    for i, ingrediente in enumerate(ingredientes):
        if not G.has_node(ingrediente):
            G.add_node(ingrediente, tipo=tipos[i])
    
    # Criar as arestas entre os ingredientes da mesma receita
    for i in range(len(ingredientes)):
        for j in range(i + 1, len(ingredientes)):
            G.add_edge(ingredientes[i], ingredientes[j])

# Calcular o coeficiente de assortatividade por tipo
assortatividade_por_tipo = nx.attribute_assortativity_coefficient(G, 'tipo')

# Exibir o coeficiente de assortatividade
print(f'Coeficiente de assortatividade por tipo: {assortatividade_por_tipo}')

# Exibir o total de nós e arestas
total_nos = len(G.nodes())
total_arestas = len(G.edges())

# Densidade da rede
densidade = nx.density(G)

print(f"\nTotal de nós: {total_nos}")
print(f"Total de arestas: {total_arestas}")
print(f"Densidade da rede: {densidade:.4f}")

# Diâmetro da rede (se a rede for conexa)
if nx.is_connected(G):
    diametro = nx.diameter(G)
    print(f"Diâmetro da rede: {diametro}")
else:
    print("A rede não é conexa, logo o diâmetro não pode ser calculado.")

# Média do comprimento dos caminhos mais curtos
comprimentos_caminho = nx.all_pairs_shortest_path_length(G)
todos_caminhos = []

for source, paths in comprimentos_caminho:
    for target, length in paths.items():
        if source != target:  # Não considerar os caminhos de um nó para ele mesmo
            todos_caminhos.append(length)

media_caminhos = np.mean(todos_caminhos)
print(f"Média do comprimento dos caminhos mais curtos: {media_caminhos:.2f}")

# Coeficiente de clustering médio
clustering_medio = nx.average_clustering(G)
print(f"Coeficiente de clustering médio: {clustering_medio:.4f}")

# Exibir os top 5 ingredientes com maior grau
degrees = dict(G.degree())
top_5_nodes = sorted(degrees, key=degrees.get, reverse=True)[:5]

top_5_table = pd.DataFrame({
    'Ingrediente': top_5_nodes,
    'Grau (Conexões)': [degrees[node] for node in top_5_nodes]
})

print("\nTop 5 ingredientes com maior grau:")
print(top_5_table)

# ==========================================
# Contar quantidade de nós e grau médio por tipo
# ==========================================
tipos_nos = {}
graus_por_tipo = {}

for node, data in G.nodes(data=True):
    tipo = data['tipo']
    grau = G.degree(node)
    
    # Atualizar contagem
    tipos_nos[tipo] = tipos_nos.get(tipo, 0) + 1
    
    # Atualizar soma dos graus
    graus_por_tipo[tipo] = graus_por_tipo.get(tipo, 0) + grau

# Agora, calcular o grau médio
print("\nQuantidade de nós e grau médio por tipo de ingrediente:")
for tipo in tipos_nos:
    quantidade = tipos_nos[tipo]
    soma_graus = graus_por_tipo[tipo]
    grau_medio = soma_graus / quantidade if quantidade > 0 else 0
    print(f"{tipo}: {quantidade} nós, grau médio = {grau_medio:.2f}")

# ========================
# Análise de Homofilia e Heterofilia
# ========================

# Co-ocorrências entre ingredientes do mesmo tipo (homofilia) e entre tipos diferentes (heterofilia)
homofilia = 0
heterofilia = 0
combinacoes_frequentes = Counter()

for u, v in G.edges():
    tipo_u = G.nodes[u]['tipo']
    tipo_v = G.nodes[v]['tipo']
    
    if tipo_u == tipo_v:
        homofilia += 1
    else:
        heterofilia += 1
    
    combinacoes_frequentes.update([(tipo_u, tipo_v)])

# Total de arestas
total_arestas = len(G.edges())

# Co-ocorrências em porcentagem
homofilia_percent = (homofilia / total_arestas) * 100
heterofilia_percent = (heterofilia / total_arestas) * 100

print(f"\nCo-ocorrências entre mesmo tipo (homofilia): {homofilia_percent:.2f}%")
print(f"Co-ocorrências entre tipos diferentes (heterofilia): {heterofilia_percent:.2f}%")

# Combinações mais frequentes entre tipos
combinacoes_frequentes_sorted = combinacoes_frequentes.most_common(10)
print("\nCombinações mais frequentes:")
for i, ((tipo_u, tipo_v), freq) in enumerate(combinacoes_frequentes_sorted):
    freq_percent = (freq / total_arestas) * 100
    print(f"{i+1}. {tipo_u} + {tipo_v}: {freq_percent:.2f}%")

# ========================
# Ingredientes centrais na culinária brasileira
# ========================

# Ingredientes centrais (os nós com maior grau)
ingredientes_centrais = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nIngredientes centrais na culinária brasileira:")
for ingrediente, grau in ingredientes_centrais:
    tipo = G.nodes[ingrediente]['tipo']
    print(f"{ingrediente} ({tipo}): conectado a {grau} outros ingredientes")

# Exibir componentes conexos (se houver mais de um)
componentes_conexos = list(nx.connected_components(G))
print(f"\nNúmero de componentes conexos: {len(componentes_conexos)}")
if len(componentes_conexos) > 1:
    print("Componentes desconectados encontrados:")
    for i, componente in enumerate(componentes_conexos, 1):
        print(f"Componente {i}: {len(componente)} nós")

# Visualizar a rede com layout de força (spring_layout)
plt.figure(figsize=(14, 14))
pos = nx.spring_layout(G, seed=42, k=1.0)

# Definir as cores dos nós de acordo com o tipo de ingrediente
node_colors = []
node_sizes = []  # Lista para os tamanhos dos nós
node_labels_sizes = {}  # Dicionário para o tamanho das fontes dos rótulos
for node in G.nodes():
    tipo = G.nodes[node]['tipo']
    color = tipo_cores.get(tipo, 'gray')
    node_colors.append(color)
    
    # Tamanho do nó proporcional ao grau (número de conexões)
    grau = G.degree(node)
    node_sizes.append(grau * 100)  # Multiplicando para um tamanho mais visível
    
    # Tamanho da fonte proporcional ao grau (baseado no número de conexões)
    node_labels_sizes[node] = 6 + grau * 0.2  # Base 6 e fator de multiplicação 0.2 para fontes menores

# Desenhar o grafo
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', alpha=0.7, linewidths=1.5)
nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.5)

# Desenhar os rótulos com tamanho proporcional ao grau
# Agora passando o dicionário de tamanhos de fontes
nx.draw_networkx_labels(G, pos, font_size=node_labels_sizes, font_color='black')

# Criar a legenda
import matplotlib.patches as mpatches
legend_labels = {tipo: mpatches.Patch(color=color, label=tipo) for tipo, color in tipo_cores.items()}
plt.legend(handles=list(legend_labels.values()), loc='upper left', fontsize=10)

plt.title("Ingredient Network by Type")
plt.axis('off')
plt.show()
