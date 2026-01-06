import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_index = random.randint(0, len(friends) - 1)
who_pay_the_bill = friends[random_index]
print(who_pay_the_bill)

choice = random.choice(friends)
print(choice)