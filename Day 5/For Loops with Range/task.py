for number in range(0,10,3):
    print(number)

print(range(0,10))


total = 0
for number in range(1,101):
    # print(number)
    total += number
print(total)


for number in range(1, 16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz\n")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
