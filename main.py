import networkx as nx
import matplotlib.pyplot as plt



G = nx.DiGraph()

codigo = '''
i = 1
if i == 1:
    print("i == 1")
else:
    print("i != 1")
'''

lista = codigo.split('\n')[1:-1]

print(lista)
print(len(lista))

# for i in range(len(lista)):
#     if 'if' in lista[i]:
#         print('if', i+1)
#         G.add_node(f'if')
#         G.add_node(f'True')
#         G.add_node(f'False')
#         G.add_node(f'final')
#         G.add_edge('if', 'True')
#         G.add_edge('if', 'False')
#         G.add_edge('True', 'final')
#         G.add_edge('False', 'final')


G.add_node(f'1')


G.add_node(f'if')
G.add_node(f'True')
G.add_node(f'False')
G.add_node(f'final')


G.add_node(f'print')


G.add_edge('1', 'if')
G.add_edge('if', 'True')
G.add_edge('if', 'False')
G.add_edge('True', 'final')
G.add_edge('False', 'final')

G.add_edge('final', 'print')

# # Adicionando nós
# G.add_node('Start')
# G.add_node('Instruction 1')
# G.add_node('Decision 1')
# G.add_node('Instruction 2')
# G.add_node('End')

# # Adicionando arestas
# G.add_edge('Start', 'Instruction 1')
# G.add_edge('Instruction 1', 'Decision 1')
# G.add_edge('Decision 1', 'Instruction 2', label='True')
# G.add_edge('Decision 1', 'End', label='False')
# G.add_edge('Instruction 2', 'End')




pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=(1000), node_color="lightblue", font_size=10, font_weight="bold", arrowsize=10)
labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig('graph.png')






