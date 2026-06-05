import string


for i in range(1,8):
    print("*"*i)
for row in range(8):
    for col in range(8):
        print("#",end=" ")
    print()
for i in range(1,11):
    print(i ,"X" ,i ,"=",i*i)
lis=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lis:
    print(i)