import csv
import os
import matplotlib.pyplot as plt


name = input("Enter your name: ")
budget = float(input("Enter your budget(in rupees): "))

expenses = []

while True:
    category = input("Enter category: ")
    if category.lower() == "done":
        break
    amount = float(input(f"Enter amount for {category} (in rupees): "))
    expenses.append((category, amount))

total_spent = sum(amount for category, amount in expenses)

print("Summary")
print("Hello,", name)
print("Your budget for today is ₹", budget)
print("Your expenses:", expenses)
print("Total spent: ₹", total_spent)

if total_spent > budget:
    print("You have exceeded your budget by ₹", total_spent - budget)
else:
    print("You are within your budget. You have ₹", budget - total_spent, "remaining.")

print("\n----- Category Totals -----")
category_totals = {}
for category, amount in expenses:
    category_totals[category] = category_totals.get(category, 0) + amount

for category, total in category_totals.items():
    print(f"{category}: ₹{total}")

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Amount"])
    writer.writerows(expenses)

print("\nExpenses saved to expenses.csv")