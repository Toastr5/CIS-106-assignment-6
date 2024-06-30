start = str(input("Do you want to calculate the first 20 units?: "))

while start != "yes":
  start = str(input("Do you want to calculate the first 20 units?: "))
#check if they want to start the program

starting_number = 0
adding_number = 1
#set the starting number to 0 and the number to add to 1
for x in range(1,20):
  starting_number = starting_number + adding_number
  adding_number = starting_number - adding_number
  with open('2.txt','a') as file:
    file.write((f"\n {starting_number}"))
#calculate the first 20 numbers of the fibonacci sequence and write them to the file