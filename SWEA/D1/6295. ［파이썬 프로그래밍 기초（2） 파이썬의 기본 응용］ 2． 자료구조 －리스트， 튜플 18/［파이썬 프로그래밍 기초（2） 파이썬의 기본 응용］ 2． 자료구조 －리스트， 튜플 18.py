row,col = map(int, input().split(','))
result = [[r*c for c in range(col)] for r in range(row)]
print(result)