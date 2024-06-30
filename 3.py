f = open("3.txt", "r")

#starting counters
total_bonus = 0

name = str(f.readline().rstrip('\n'))

while name != "":
  salary = float(f.readline())
  if salary >= 100000:
    bonus_rate = 0.2
  elif salary < 100000 and salary >= 50000:
    bonus_rate = 0.15
  else:
    bonus_rate = .1
  bonus = salary * bonus_rate
  total_bonus = total_bonus + bonus
  print(f"{name}")
  print(f"Salary: ${salary}")
  print(f"bonus rate: {bonus_rate*100}%")
  print(f"bonus: ${bonus}")
  name = str(f.readline().rstrip('\n'))
print(f"Total bonus: ${total_bonus}")
  
  