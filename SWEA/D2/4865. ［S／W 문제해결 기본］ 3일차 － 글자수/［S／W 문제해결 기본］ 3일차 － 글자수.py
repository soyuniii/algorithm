T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    dic = {}
    
    for s in str1:
        dic[s] = str2.count(s)
    
    result = max(dic.values())
        
    print(f"#{test_case} {result}")
            