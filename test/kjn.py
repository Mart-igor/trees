# def count_connected_components(grid):
#     if not grid:
#         return 0
    
#     n = len(grid)
#     m = len(grid[0])
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     count = 0
    
#     # Направления для обхода соседних ячеек (вверх, вниз, влево, вправо)
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     def dfs(i, j):
#         if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or visited[i][j]:
#             return
#         visited[i][j] = True
#         for direction in directions:
#             dfs(i + direction[0], j + direction[1])
    
#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] == 1 and not visited[i][j]:
#                 dfs(i, j)
#                 count += 1
    
#     return count

def mark_connected_components(grid):
    if not grid:
        return grid
    
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    current_char = 'A'  # Начинаем с первой буквы алфавита
    
    def dfs(i, j, char):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1 or visited[i][j]:
            return
        visited[i][j] = True
        grid[i][j] = char  # Помечаем ячейку текущей буквой
        for direction in directions:
            dfs(i + direction[0], j + direction[1], char)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, current_char)
                current_char = chr(ord(current_char) + 1)  # Переходим к следующей букве
    
    return grid
# Пример использования
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

print(mark_connected_components(grid))  # Вывод: 3


def count(grid):
    if not grid:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    visited = [[0] * m for _ in range(n)]

    count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(i, j, A):
        if i < 0 or i >= n or j < 0 or j >=m or visited[i][j] or grid[i][j] == 0:
            return
        visited[i][j] = A
        for direction in directions:
            dfs(i + direction[0], j + direction[1])

    for i in range(len(n)):
        for j in range(len(m)):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, 'A')
                count += 1
                c = chr(ord(char) + 1)

    return count


def searche(graph):
    visited = set()

    def dfs(v, parent):
        for vv in graph[v]:


    for v in graph:
        if v not in visited:
            if dfs(graph, v):
                return True
            






def has_cyrcle(graph):
    visited = set()
    rec = []

    def dfs(v):
        visited.add(v)
        rec.append(v)
        for vv in graph[v]:
            if vv not in visited:
                if dfs(vv):
                    return True
            elif vv in rec:
                return True

    rec = []

    for v in graph:
        if v not in visited:
            if dfs(v):
                return True
    return False