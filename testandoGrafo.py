import networkx as nx
import matplotlib.pyplot as plt

matriz = [
    [0, 1, 1, 0, 0, 0, 0, 1], # 0
    [0, 0, 0, 1, 0, 0, 0, 1], # 1
    [0, 0, 0, 0, 1, 0, 0, 1], # 2
    [0, 0, 0, 0, 0, 1, 0, 1], # 3
    [0, 0, 0, 0, 0, 0, 1, 1], # 4
    [0, 0, 0, 0, 0, 0, 0, 1], # 5
    [0, 0, 0, 0, 0, 0, 0, 1], # 6
    [0, 0, 0, 0, 0, 0, 0, 1], # 7
]


G = nx.DiGraph()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            G.add_edge(i, j)
            
            
## create image
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("path.png")
# nx.draw(G, with_labels=True, font_weight='bold')