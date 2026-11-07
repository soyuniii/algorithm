from itertools import permutations

def solution(numbers):
    # 아이디어: 문자열 떼어내서 조합해서 소수인지 확인
    # 1. 문자열 떼어내서 숫자 리스트로
    answer = set()
    ls = [int(s) for s in numbers] 
    # 2. 모든 수 조합을 - 튜플 -> 숫자 변형 -> set에 넣어서 중복제거
    for i in range(1, len(numbers)+1):
        for p in permutations(ls, i):
            answer.add(int(''.join(map(str, p))))
            
    #3. 소수인지 확인 (소수: 1, 자기자신으로만 나누어 떨어짐)
    
    prime_count = 0
    
    for a in answer:
        if a < 2:
            continue
            
        is_prime = True
        
        for i in range(2, int(a ** 0.5)+1):
            if a % i == 0:
                is_prime = False
                break
                
        if is_prime:
            prime_count += 1
            
    return prime_count

    