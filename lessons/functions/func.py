def name_generator ():
    first_name ="Idrish"
    last_name="Katwara"
    space=" "
    f=first_name + space + last_name
    print(f)
    return f
name_generator ()
def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
#even numbers
def even_number(n):
    even=[]
    for i in range(n+1):
        if i%2==0:
            even.append(i)
    return(even)
print(even_number(10))
#func with default parameter
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('IK'))

#age
def calculate_age (birth_year,current_year = 2026):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))
print("AGE :",calculate_age(2007,2026))
#sum arbitary nu of arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2,3)) # 10
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Asabeneh','Brook','David','Eyob')