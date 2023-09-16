n = int(input())

grid = []
for i in range(n):
    row = input().strip()
    row_chars = list(row)
    grid.append(row_chars)

DP = [[0] * n for _ in range(n)]
