def dfs(x, y):
    if x == n-1 and y == n-1:
        return True  # Found a path to 't'

    # Mark the current cell as visited or memoize it to avoid revisiting
    visited[x][y] = True

    # Define possible movements (rightwards, downwards, leftwards, upwards)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]

        # Check if the new position is within bounds and not visited and walkable
        if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] != '#':
            if dfs(new_x, new_y):
                return True  # If a path to 't' is found, exit

    return False  # No path to 't' found from this cell

n = int(input())

grid = []
for i in range(n):
    row = input().strip()
    row_chars = list(row)
    grid.append(row_chars)

DP = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            DP[i][j] = 1

        elif grid[i][j] == '#':
            DP[i][j] = 0

        else:
            if i > 0 and j > 0:
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
            elif i == 0:
                DP[i][j] += DP[i][j-1]
            else:
                DP[i][j] += DP[i-1][j]

if DP[n-1][n-1] != 0:
    print(DP[n-1][n-1])
else:
    visited = [[False] * n for _ in range(n)]
    if dfs(0, 0):
        print("THE GAME IS A LIE")
    else:
        print("INCONCEIVABLE")




