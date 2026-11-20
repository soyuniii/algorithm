def fibo(ls, n):
    for i in range(n-2):
        ls[i+2] = ls[i]+ls[i+1]
    print(ls)


num = int(input())
result = [0] * num
result[0] = 1
result[1] = 1

fibo(result, num)