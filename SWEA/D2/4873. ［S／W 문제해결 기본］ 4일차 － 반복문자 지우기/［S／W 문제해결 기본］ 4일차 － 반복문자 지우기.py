T = int(input())

for test_case in range(1, T + 1):
    string = input()
    stack = []
    
    # 스택 사용? i가 스택에 없으면 추가, 있다면 pop -> ABCCB -> ABB -> A
	# 반복 기준? 문자열 길이만큼
    # stack의 가장 위에 있는 수랑 비교해야함
    # stack[-1] -> stack에 아무것도 없을떄 처리
    for s in string:
        if not stack or s is not stack[-1]:
            stack.append(s)
        else:
            stack.pop()
            
    print(f"#{test_case} {len(stack)}")
