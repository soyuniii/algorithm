data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {}

for d in data:
    if d in result:
        result[d] += 1
    else:
        result[d] = 1

print(result)