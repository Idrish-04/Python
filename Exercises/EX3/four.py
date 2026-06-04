"""n=int(input("Enter number:  "))#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")
#Check if type of '10' is equal to type of 10
a="10"
b=10
print(type(a)==type(b))"""
"""Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
"""hours=int(input("Enter hours:  "))
rate_per_hour=int(input("Enter rate per hour:  "))
pay=hours*rate_per_hour
print("The pay of the person is:", pay)"""
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years=int(input("Enter number of years you have lived:  "))
seconds=years*365*24*60*60
print("You have lived for ", seconds, " seconds.")
#Write a Python script that displays the following table
"""1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""
for i in range(1,6):
    print(i, 1,i**2,i**3,i**4)
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
print('Days\tTopics\tExercises')
print('This is a backslash  symbol (\\)')