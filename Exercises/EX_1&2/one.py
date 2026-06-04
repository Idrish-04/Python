first_name="IDRISH"
last_name="Katwara"
full_name=first_name+" "+last_name
country="India"
age=22
year=2026
is_married=False
is_true=True
is_light_on=False
first_name,last_name,full_name="Idrish","Katwara","Idrish Katwara"
print(first_name)
print(last_name)
print(full_name)
print(len(first_name))
if len(first_name)>len(last_name):
    print("First name is longer than last name")
elif len(first_name)<len(last_name):
    print("Last name is longer than first name")
else:
    print("First name and last name are of equal length")
num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
exp=num_one**num_two
floor_division=num_one//num_two
print("Total:",total)
print("Difference:",diff)
print("Product:",product)
print("Division:",division)
print("Remainder:",remainder)
print("Exponentiation:",exp)
print("Floor Division:",floor_division)
#radius of circle=30
radius=30
area_of_circle=3.14*radius**2
print("Area of Circle:",int(area_of_circle))
circumference_of_circle=2*3.14*radius
print("Circumference of Circle:",int(circumference_of_circle))
"""radius=int(input("Enter radius of circle: "))
area_of_circle=3.14*radius**2
print("Area of Circle:",int(area_of_circle))
circumference_of_circle=2*3.14*radius
print("Circumference of Circle:",int(circumference_of_circle))"""
help("keywords")