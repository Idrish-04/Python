age=int(input("Enter your age: "))
if age>=18:
    print(" You are old enough to drive")
else:
    print(f'you need {18-age} more years to learn to drive')
#2
my_age=int(input("Enter your age : "))
your_age=int(input("Enter your age : "))
if my_age>your_age:
    diff=my_age-your_age
    if diff==1:
        print(f'I am {diff}year older than you')
    else:
        print(f"i am {diff} years older than you")
elif your_age > my_age:
    diff=your_age-my_age
    if diff == 1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} years older than me.")

else:
    print("We are the same age.")
