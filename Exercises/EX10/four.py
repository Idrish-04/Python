even_total = 0
odd_total = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
print(f'The sum of even number is {even_total}.and sum of odd number is {odd_total}')