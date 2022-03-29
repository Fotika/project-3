import os.path
file_name=input("Enter file me:",)
# Assigning values to rows,columns and price
rows = 9
columns = 20
price = 20
seats = 0
theater = [[0]*columns for i in range(rows)]
with open("theater.txt", "r") as f:
    for line in f:
        # reading the rows and columns
        a,b=map(int,line.split())
        theater[a-1][b-1]= 1
        # incremental seats
        seats+=1
# checking for the right file.
while (os.path.isfile (file_name) == False):
    print("Error-File not found")
    file_name = input("Enter file me:",)
    continue

for i in range(rows):
    for j in range(columns):
        if theater [i][j]==0:
            print('_',sep='',end='')
        else:
            print('x',sep='',end='')
    print()
print()
# print number of seats
print("number of ticket:",seats)
# print revenue
print('Revenue:$' + str(seats * price))


