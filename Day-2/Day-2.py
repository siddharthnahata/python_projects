print("Welcome to tip Calculator!")

bill_amount = float(input("Please enter your total bill amount: "))
tip_percentage = float(input("Please enter percentage of tip you want to give: "))
total_tip = bill_amount * tip_percentage / 100
print(f"Your tip amount is: {round(total_tip, 2)}")
total_bill = bill_amount + total_tip
print(f"Your Total payment includeing Tip will be: {round(total_bill, 2)}")
split_in = float(input("In how many people will you spliting the Bill: "))
split_share_per = round((total_bill / split_in), 2)
print(f"Your per Individual split will be: {split_share_per}") 