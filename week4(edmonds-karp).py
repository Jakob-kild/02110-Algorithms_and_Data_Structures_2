## Download speed problem
# bfs search in augmented paths
from dataclasses import dataclass
from collections import deque

@dataclass
class EdgeInfo:
    edge_from: int
    edge_to: int
    id: int
    forward: bool

class FlowGraph:
    def __init__(self, number_of_nodes):
        self.adjacency_list = [[] for _ in range(number_of_nodes)]
        self.flow = []
        self.capacity = []

    def add_edge(self, edge_from, edge_to, capacity):
        self.adjacency_list[edge_from].append(EdgeInfo(edge_from, edge_to, len(self.flow), True))
        self.adjacency_list[edge_to].append(EdgeInfo(edge_to, edge_from, len(self.flow), False))
        self.flow.append(0)
        self.capacity.append(capacity)

    def add_flow(self, edge_info, flow):
        if edge_info.forward:
            self.flow[edge_info.id] += flow
        else:
            self.flow[edge_info.id] -= flow

    #wether or not i can traverse this edge
    def traversable(self, edge):
        return self.leftover_capacity(edge) > 0

    def leftover_capacity(self, edge):
        if edge.forward:
            return self.capacity[edge.id] - self.flow[edge.id]
        else:
            return self.flow[edge.id]

def bfs(graph, n, source, dest):
    edge_taken = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[source] = True
    queue = deque()
    queue.append(source)

    while queue:
        v = queue.popleft()
        for edge in graph.adjacency_list[v]:
            if graph.traversable(edge) and not visited[edge.edge_to]:
                visited[edge.edge_to] = True
                edge_taken[edge.edge_to] = edge
                queue.append(edge.edge_to)

    if visited[dest]:
        #extract path
        edges_used = []
        node = dest
        while edge_taken[node]:
            edges_used.append(edge_taken[node])
            node = edge_taken[node].edge_from
        return edges_used
    return None

def edmonds_karp(graph, n, source, dest):
    #while there is an augmenting path
    while True:
        path = bfs(graph, n, source, dest)
        if path is None:
            break
        flow = graph.leftover_capacity(path[0])
        for edge in path:
            flow = min(flow, graph.leftover_capacity(edge))
        for edge in path:
            graph.add_flow(edge, flow)

    total_flow = 0
    for edge in graph.adjacency_list[source]:
        if edge.forward:
            total_flow += graph.flow[edge.id]

    return total_flow

n, m = map(int, input().split())

graph = FlowGraph(n)
for _ in range(m):
    v, u, c = map(int, input().split())
    v -= 1
    u -= 1
    graph.add_edge(v, u, c)

flow = edmonds_karp(graph, n, 0, n-1)
print(flow)













