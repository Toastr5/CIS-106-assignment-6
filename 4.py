f = open("4.txt", "r")

#starting counters
summed_extended_price = 0
total_orders = 0
total_quanitity = 0
#read the first line
item = str(f.readline().rstrip('\n'))

#while loop
while item != "":
  price = int(f.readline().rstrip('\n'))
  quantity = int(f.readline().rstrip('\n'))
  extended_price = price * quantity
  summed_extended_price = summed_extended_price + extended_price
  total_orders = total_orders + 1
  total_quanitity = total_quanitity + quantity
  print(f"{item}")
  print(f"Price per unit: ${price}")
  print(f"Quantity: {quantity}")
  print(f"Extended price: ${extended_price}")
  item = str(f.readline().rstrip('\n'))

#print totals and averages
print("\n")
print(f"Total orders: {total_orders}")
print(f"Total extended price: ${summed_extended_price}")
print(f"Average order price: ${summed_extended_price/total_orders}")
