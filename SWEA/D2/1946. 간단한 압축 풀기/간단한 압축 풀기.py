T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    dic = {}
    result = ""
    for _ in range(n):
        a,b = input().split()
        dic[a] = b


    for k,v in dic.items():
        result += k*int(v)

    print(f"#{test_case}")

    for i in range(0,len(result),10):
        print(result[i:i+10])