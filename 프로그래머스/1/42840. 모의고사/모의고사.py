def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == p1[i % 5]:
            result[1] += 1
        if answers[i] == p2[i % 8]:
            result[2] += 1
        if answers[i] == p3[i % 10]:
            result[3] += 1
            
    max_score = max(result.values())
    
    answer = []
    for person, score in result.items():
        if score == max_score:  
            answer.append(person)
            
    return sorted(answer)
    
    