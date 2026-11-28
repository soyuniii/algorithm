def solution(records):
    result = []
    uid_to_name = {}
    
    # uid별 최종 닉네임 정리
    for record in records:
        do, uid, *rest = record.split()

        if do != 'Leave':
            uid_to_name[uid] = rest[0] #nickname
        
    # 출력
    for record in records:
        do, uid, *rest = record.split()
        if do == 'Enter':
            result.append(f"{uid_to_name[uid]}님이 들어왔습니다.")
        elif do == 'Leave':
            result.append(f"{uid_to_name[uid]}님이 나갔습니다.")
        else:
            continue
    
    return result
