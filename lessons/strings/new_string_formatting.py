first_name="IDRISH" 
last_name="KATWARA"
language="PYTHON"
formated_string1=f"I am {first_name} {last_name}. I teach {language}."
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string1)
print(formated_string)

a=4
b=2
print('{}+{}={}'.format(a,b,a+b))
print(f"{a}+{b}={a+b}")

radius=192
pi=3.14
area=pi*radius**2
print(f'the area of circle with radius {radius} is {area:.2f}')
print('the area of circle with radius {} is {:.2f}'.format(radius,area))