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
average=sum(ages)/len(ages)
print("Average :",average)
range=max(ages)-min(ages)
print(range)
min_diff=round(abs(min(ages)-average),2)
max_diff=round(abs(max(ages)-average),2)
print(min_diff)
print(max_diff)
#abs() converts negative values to positive values.
