#if condition
a=3
if a>0:
    print("A is a positive number")
elif a==0:
    print("a is zero")
else:
    print("A is a negative number")

#shorthand
a=4
print("a is  positive")if a>0 else print("a is negative")
#nested
if a >0:
    if a%2==0:
        print("A is  positive nd even int")
    else:
        print("a is positive num")
elif a==0:
    print("a is zero")
else:
    print("a is negative num")
#if cond and logical operator
if a>0 and a%2==0:
    print("A is an even and positive integer")
elif a>0 and a%2!=0:
    print("a is pos nnum")
elif a==0:
    print("a is zero")
else:
    print("a is neg num")
#if and or logical
User="IK"
access=31
if User=="IK" or access==31:
    print("Access granted")
else:
    print("Access denied")