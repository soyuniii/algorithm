dp = [0]*31 # 10으로 나눈 몫
dp[1] = 1
dp[2] = 3
for i in range(3, 31):
    dp[i] = dp[i-1] + 2 * dp[i-2]

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) 
    # a(20,10) b(20,20)일때
    # 마지막에 a 놓는다면 
    # 마지막에 b or aa 놓는다면
    # n 채우는 경우의 수 =  (n-10)경우 +2 * (n-20)경우
    # n=10 ->1, n=20 ->  3 (1+2*1) , n=30 -> (n=20 결과) +2*(n=10결과)
    print(f"#{test_case} {dp[n//10]}")
    
