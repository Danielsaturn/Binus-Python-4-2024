usernum = int(input("Please enter a number: "))


for row in range(usernum, 0, -1):
    
    for j in range(1, row + 1):
        print(row, end="")
    print()
for i in range(1, usernum + 1):
    
    for j in range(1, i + 1):
        print(i, end="")
    print()
