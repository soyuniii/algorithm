def solution(phone_book):
    
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = True
        
    for phone in phone_book:
        temp = ""
        for char in phone[:-1]:
            temp += char
            if temp in hash_map:
                return False
            
    return True
        
        