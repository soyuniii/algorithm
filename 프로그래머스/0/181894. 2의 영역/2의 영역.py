def solution(arr):
    idx = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    return arr[idx[0]:idx[-1]+1]  if idx else [-1]
            