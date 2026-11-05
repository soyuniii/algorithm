def solution(progresses, speeds):
    stack = []
    for progress, speed in zip(progresses, speeds):
        day = 0
        while(progress < 100):
            progress += speed
            day += 1
        stack.append(day)
        
    result = []
    standard = stack[0]
    num = 1
    
    for i in range(1, len(stack)):
        if standard >= stack[i]:
            num += 1
        else:
            result.append(num)
            standard = stack[i]
            num = 1
            
    result.append(num)
    return result
            
            
    
    
        
        
        