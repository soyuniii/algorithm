store = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

sort_items = sorted(store.items(),key= lambda item: item[1], reverse=True)

for k,v in sort_items:
    print(f"{k}: {v}")