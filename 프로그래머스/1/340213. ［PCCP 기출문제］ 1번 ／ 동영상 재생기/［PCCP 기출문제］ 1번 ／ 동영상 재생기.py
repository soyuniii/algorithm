def solution(video_len, pos, op_start, op_end, commands):
    
    def to_sec(time_str):
        m,s = map(int, time_str.split(":"))
        return m * 60 + s
    
    def to_str(total_sec):
        m = total_sec // 60
        s = total_sec % 60
        return f"{m:02d}:{s:02d}"
    
    video_len, pos, op_start, op_end = map(to_sec, [video_len, pos, op_start, op_end])
          
    for c in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        
        if c == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
            
        if c == "next":
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10
            
        
    if op_start <= pos <= op_end:
            pos = op_end

    
    return to_str(pos)