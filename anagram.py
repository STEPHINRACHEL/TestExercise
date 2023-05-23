str1 = input().strip() # integral
str2 = input().strip() #triangle

flag = True

for ch in str1:
    if ch not in str2:
        flag = False
        break

if flag:
    print("Anagram")
else:
    print("Not an Anagram")
