def solution(message, spoiler_ranges):
    words = message.split(' ')
    
    word_infos = []
    current_idx = 0
    
    for word in words:
        start = message.find(word, current_idx)
        end = start + len(word)-1
        
        word_infos.append({
            'word' : word,
            'start' : start,
            'end' : end
        })
        current_idx = end + 1
    
    spoiler_idx = set()
    for s, e in spoiler_ranges:
        for idx in range(s, e+1):
            spoiler_idx.add(idx)
            
    normal_words = set()
    
    for info in word_infos:
        word = info['word']
        w_start = info['start']
        w_end = info['end']
        
        is_spoiler_word = False
        for idx in range(w_start, w_end+1):
            if idx in spoiler_idx:
                is_spoiler_word = True
                break
                
        if not is_spoiler_word:
            normal_words.add(word)
    
    answer = 0
    revealed_words = set()
    
    for s,e in spoiler_ranges:
        for info in word_infos:
            w_start = info['start']
            w_end = info['end']
            word = info['word']
            
            if not (w_end<s or w_start>e):
                if word not in normal_words and word not in revealed_words:
                    revealed_words.add(word)
                    answer += 1
                    
    return answer
    
    