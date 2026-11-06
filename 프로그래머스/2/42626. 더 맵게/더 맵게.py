import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while len(scoville) >= 2 and scoville[0] < K:
        low1 = heapq.heappop(scoville)
        low2 = heapq.heappop(scoville)
        mix = low1 + low2 * 2
        heapq.heappush(scoville, mix)
        count += 1
    
    
    return -1 if scoville[0] < K else count