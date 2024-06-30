start = str(input("Do you want to start?: "))

while start != "yes":
  start = str(input("Do you want to start?: "))
#check if they want to start the program
year = 0
principle_ammount = int(input("Give principle ammount: "))
interest_rate = float(input("Give interest rate in decimal form: "))
beginning_balance = principle_ammount
total_intrest = 0
ending_balance = 0
for year in range (0,5):
  year = year + 1
  intrest_made = beginning_balance * interest_rate
  ending_balance = beginning_balance + intrest_made
  print(f"Year: {year}")
  print(f"Beginning Balance: {beginning_balance}")
  print(f"Intrest Made: {intrest_made}")
  print(f"Ending Balance: {ending_balance}")
  beginning_balance = ending_balance
  total_intrest =  total_intrest +intrest_made
  print("\n")
print(f"Total intrest made: {total_intrest}")