result = []
for i in range(100,301):
    if all(int(ch) % 2 == 0 for ch in str(i)):
        result.append(str(i))

print(",".join(result))