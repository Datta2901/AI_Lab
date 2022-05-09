graph = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'f'],
    'd' : ['b','e'],
    'e' : ['g','d','b'],
    'f' : ['c','g'],
    'g' : [ 'e','f'] 
}
visited = set() 
def dfs(visited, graph, node): 
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

if __name__ == '__main__':
  print("Depth-First Search Traversal")
  dfs(visited, graph, 'a')
  print()