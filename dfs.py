# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['3', '2' , '1']),
         '1': set(['2', '0']),
         '2': set(['4', '1', '0']),
         '3': set(['0']),
         '4': set(['2'])}

dfs(graph, '0')