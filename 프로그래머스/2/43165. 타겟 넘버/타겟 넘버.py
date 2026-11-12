
def solution(numbers, target):
    answer = 0 # 방법의 수
    
    def dfs(idx, current_sum):
        nonlocal answer
        # 종료 조건
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        # 다음 더하기
        dfs(idx+1, current_sum + numbers[idx])
        # 다음 빼기
        dfs(idx+1, current_sum - numbers[idx])
        
    dfs(0,0) # 0번째 누적합0
    
    return answer
    

    
        