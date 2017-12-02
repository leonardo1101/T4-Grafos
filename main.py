import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from dijkstra import mst_dijkstra


A = np.loadtxt('wg59_dist.txt', dtype=int)

r = [1, 32]
G = nx.from_numpy_matrix(A)
mst = mst_dijkstra(G, r)
nx.draw(mst, with_labels=True)
plt.draw()
plt.show()


r = [0, 30, 55]
G = nx.from_numpy_matrix(A)
mst = mst_dijkstra(G, r)
nx.draw(mst, with_labels=True)
plt.draw()
plt.show()