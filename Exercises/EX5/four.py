ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print("Min age: ", min_age)
print("Max age: ", max_age)
#median age (one middle  item or two middle items div by two)
ages.sort()
n=len(ages)
if n%2==0:
    median=(ages[n//2 - 1] + ages[n//2]/2)
else:
    median=ages[n//2]
print("Median ages ",median)
#average
