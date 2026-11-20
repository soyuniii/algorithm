s = input().strip()
c = ""

if s.isalpha():
    if s.isupper():
        c = s.lower()
    else:
        c = s.upper()
else:
    c = s

print(f"{s}(ASCII: {ord(s)}) => {c}(ASCII: {(ord(c))})")