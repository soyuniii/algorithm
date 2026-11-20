def biggest(*args):
    return max(args)

a = (3,5,4,1,8,10,2)
print(f"max{a} => {biggest(*a)}")