str1 = input().strip() # integral
str2 = input().strip() #triangle

flag = True
string1 = sorted(list(str1.lower().replace(" ", "")))
string2 = sorted(list(str2.lower().replace(" ", "")))

if len(string1) == len(string2):
    for ch in str1:
        if ch not in str2:
            flag = False
            break
else:
    flag = False

if flag:
    print("Anagram")
else:
    print("Not an Anagram")
