sum_evens = 0
sum_odds = 0

for i in range(0, 101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"Sum of all even numbers (0-100): {sum_evens}")
print(f"Sum of all odd numbers (0-100): {sum_odds}")
