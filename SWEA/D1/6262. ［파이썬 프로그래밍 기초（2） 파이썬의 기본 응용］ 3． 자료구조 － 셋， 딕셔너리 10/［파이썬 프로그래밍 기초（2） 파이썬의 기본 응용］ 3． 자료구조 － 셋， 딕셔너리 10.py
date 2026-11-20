string = input()
count = {}

for s in string:
    if s in count.keys():
        count[s] += 1
    else:
        count[s] = 1

for k,v in count.items():
    print(f"{k},{v}")