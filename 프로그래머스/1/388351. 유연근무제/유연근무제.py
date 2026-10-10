def solution(schedules, timelogs, startday):
    result = 0
    
    def to_min(time):
        h = time // 100
        m = time % 100
        return h*60+m
    
    for s, log in zip(schedules, timelogs):
        success = True
        current_day = startday
        
        for time in log:
            if current_day not in (6,7):
                # 허용 시간 계산
                allow_time = to_min(s) + 10
                time = to_min(time)
                
                # 지각한 경우
                if time > allow_time:
                    success = False
                    break
            
            current_day = (current_day%7)+1
            
        if success:
            result += 1
                
    return result
        
    
                        
                    
                
            