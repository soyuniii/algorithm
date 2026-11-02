def solution(n, slicer, num_list):
    a, b, c = slicer[0], slicer[1], slicer[2]
    match n:
        case 1: return num_list[:b+1]
        case 2: return num_list[a:]
        case 3: return num_list[a:b+1]
        case 4: return num_list[a:b+1:c]
    