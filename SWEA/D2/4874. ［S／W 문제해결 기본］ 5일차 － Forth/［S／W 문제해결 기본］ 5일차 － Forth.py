T = int(input())

for test_case in range(1, T + 1):
    code_list = list(input().split())
    stack=[]
    operator = ["+", "-", "*", "/"]
    result = 0
    is_error = False # 연산 안되는 경우
    
    for code in code_list:
        if code.isdigit(): #피연산자
            stack.append(int(code))
       	elif code in operator: #연산자
                if len(stack) < 2:
                    is_error = True
                    break
                b = stack.pop()
                a = stack.pop()
                
                if code == operator[0]:
                    stack.append(a+b)
                elif code == operator[1]:
                    stack.append(a-b)
                elif code == operator[2]:
                    stack.append(a*b)
                elif code == operator[3]:
                    stack.append(a//b)
        elif code == ".":
            if len(stack) != 1:
                is_error = True
            result = stack.pop()
            break
            
    print(f"#{test_case} {result}") if not is_error else print(f"#{test_case} error")
            
