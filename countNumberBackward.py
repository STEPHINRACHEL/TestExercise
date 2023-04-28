# Write a program in Python or Java that counts backwards from 100 to 1 and prints:
# “Agile” if the number is divisible by 5,“Software” if the number is divisible by 3,
# “Testing” if the number is divisible by both,
# or prints just the number if none of those cases are true


for i in range(100, 0, -1):
    if i % 5 == 0 and i % 3 == 0:
        print("Testing")
    elif i % 5 == 0:
        print("Agile")
    elif i % 3 == 0:
        print("Software")
    else:
        print(i)

