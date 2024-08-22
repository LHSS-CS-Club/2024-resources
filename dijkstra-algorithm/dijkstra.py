# Dijkstras algorithm that will compute the shortest path in a graph. For each node, it will display the path it took to get to the end.

# If you are looking for a faster implementation than this, look into dijkstra's algorithm with min-max heaps/priority queue. (this runs in O(n^2) time on average, min-max heaps runs in O(n log n))

# Check the repo for the implementation with priority queue (in Java)

class Dijkstras:
  def __init__(self, nodeStart, nodeFinal, g: dict):
    self.startNode = nodeStart
    self.targetNode = nodeFinal
    self.graph = g

  def __defineSymmetry__(self, graph: dict):
    nodes = list(graph.keys())

    for node in nodes:
      for connected, weight in graph[node]:
        if connected not in graph:
          graph[connected] = []
        graph[connected].append((node, weight))

    return graph

  def shortestPathDijkstras(self):
    graph = self.__defineSymmetry__(self.graph)
    n = len(graph)
    nodes = list(graph.keys())
    values = [float('inf') for i in range(n)]
    visited = [False for i in range(n)]

    currNode = self.startNode
    values[currNode] = 0

    for node in range(n):
      lowest = float('inf')

      for connected, weight in graph[currNode]:
        if values[currNode] + weight < values[connected]:
          values[connected] = values[currNode] + weight

        if values[connected] < lowest and not visited[connected]:
          lowest = values[connected]
          nextNode = connected

      visited[currNode] = True
      currNode = nextNode

    if values[self.targetNode] == float('inf'):
      return 'No path to end node'
    else:
      return f'The shortest distance to node {self.targetNode} is {values[self.targetNode]}'

dijkstras = Dijkstras(0, 3, {
  0: [(1, 4)],
  1: [(2, 4), (3, 3)],
  2: [(3, 6), (1, 3)],
  3: [(0, 6)]
})

print(dijkstras.shortestPathDijkstras())