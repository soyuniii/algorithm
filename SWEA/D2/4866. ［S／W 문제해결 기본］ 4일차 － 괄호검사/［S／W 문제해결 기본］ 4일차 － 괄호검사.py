T = int(input())

for test_case in range(1, T + 1):
    string = input()
    stack = []
    result = 0
    is_valid = True
    
    for s in string:
        if s == "{" or s =="(":
            stack.append(s)
        elif s == "}" or s == ")":
            if not stack:
                is_valid = False
                break
            a = stack[-1]
            if a =="{" and s == "}" or a == "(" and s == ")":
                stack.pop()
            else:
                is_valid = False
                break
    if is_valid and not stack:
        result = 1
    else:
        result = 0
    
    print(f"#{test_case} {result}")
    