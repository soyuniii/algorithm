def find_num(lst, n):
    if n in lst:
        return True
    else:
        return False
    
lst = [2,4,6,8,10]
print(lst)
print(f"{5} => {find_num(lst, 5)}")
print(f"{10} => {find_num(lst, 10)}")
    