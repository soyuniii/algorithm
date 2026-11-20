nlist=[]

for dan in range(2,10):
    dan_list = [dan*i for i in range(1,10) if not dan*i % 3 == 0 and not dan*i % 7 == 0]
    nlist.append(dan_list)
print(nlist)