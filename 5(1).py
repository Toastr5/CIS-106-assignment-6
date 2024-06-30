from re import I


f = open("5.txt", "r")
#starting counters

total_students = 0
total_tuition = 0

name = str(f.readline().rstrip('\n'))
while name != "":
  district = str(f.readline().rstrip('\n'))
  credit_cost = 0
  if district == I:
    credit_cost = 250
  else:
    credit_cost = 500
  credits = int(f.readline().rstrip('\n'))
  student_tuition = credit_cost * credits
  print(f"{name}")
  print(f"Credits:{credits}")
  print(f"Tuition: ${student_tuition}")
  total_tuition = total_tuition + student_tuition
  total_students = total_students + 1
  name = str(f.readline().rstrip('\n'))

#exit loop
print("\n")
print(f"Total Students: {total_students}")
print(f"Total Tuition: ${total_tuition}")