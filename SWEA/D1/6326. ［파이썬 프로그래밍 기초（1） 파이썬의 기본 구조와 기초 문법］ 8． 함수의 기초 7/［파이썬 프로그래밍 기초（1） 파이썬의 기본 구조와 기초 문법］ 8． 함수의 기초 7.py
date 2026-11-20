def factorial(n):
     return n * factorial(n-1) if not n == 1 else 1

num = int(input())
print(factorial(num))