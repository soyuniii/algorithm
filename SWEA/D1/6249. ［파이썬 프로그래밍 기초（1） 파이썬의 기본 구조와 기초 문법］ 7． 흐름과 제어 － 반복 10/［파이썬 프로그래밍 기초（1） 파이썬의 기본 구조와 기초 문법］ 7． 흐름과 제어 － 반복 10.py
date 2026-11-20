n = int(input())
count = {i:0 for i in range(10)}

for s in str(n):
    count[int(s)] += 1

print(' '.join(map(str, count.keys())))
print(' '.join(map(str, count.values())))