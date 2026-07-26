#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 15 20 25 "))
people = int(input("How many people to split the bill? "))

total_per_person = round((bill/people) *(1+tip/100), 2)

print(f"Each person should pay: ${total_per_person}")
