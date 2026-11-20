alist = [i for i in range(1,11)]
evens =list(filter(lambda x: x % 2 == 0, alist))
result = list(map(lambda x: x*x, evens))
print(result)