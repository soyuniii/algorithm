n = int(input())
result = []

for i in range(1, n+1):
    s = str(i)
    clap = sum(1 for c in s if c in ('3','6','9'))
    if clap > 0:
        result.append('-'*clap)
    else:
        result.append(s)

print(' '.join(result))