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