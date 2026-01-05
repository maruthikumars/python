from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100

tip_amount = bill * tip_percentage
final_bill = bill + tip_amount

each_person_bill = round(final_bill / people, 2)

print(f"Each person should pay: ${each_person_bill}")



