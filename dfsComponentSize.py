def dfsComponentSize(matrix, vertex):

    def dfs(currentVertex, visited):
        visited[currentVertex] = True
        componentSize = 1
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                componentSize += dfs(nextVertex, visited)
        return componentSize

    visited = []

    for i in range(len(matrix)):
        visited.append(False)

    componentSize = dfs(vertex, visited)

    return componentSize
