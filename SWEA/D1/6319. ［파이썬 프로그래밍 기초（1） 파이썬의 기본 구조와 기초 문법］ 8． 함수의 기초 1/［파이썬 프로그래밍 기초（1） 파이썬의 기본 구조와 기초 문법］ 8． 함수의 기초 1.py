def check(s):
    rs = ""
    for i in range(len(s)-1, -1,-1):
        rs += s[i]
    return rs

s = input().strip()
print(s)

if s  == check(s):
    print("입력하신 단어는 회문(Palindrome)입니다.")


