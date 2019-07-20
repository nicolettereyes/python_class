
OUT_OF_BOUNDS = float('-inf')
# print(OUT_OF_BOUNDS)

def calculate(first_number, second_number, operater):
    result = 0
    if operater == "+":
        result = (first_number + second_number) 
    elif operater == "-":
        result = (first_number - second_number) 
    elif operater == "*":
        result = (first_number * second_number)
    elif operater == "/":
        result = (first_number / second_number)  
    else:
        result = OUT_OF_BOUNDS     
    return result

#print(calculate(1,2,'+'))


more_input = True
while more_input:
  first_number = input("What is the first number? ") 
  first_number = int(first_number)
  second_number = input("What is the second number? ")
  second_number = int(second_number)

  operater = input("What operation do you want me to do (+,-,*, /)? ")
  operater = operater.strip()
  
  result = calculate(first_number, second_number, operater)

  if result == OUT_OF_BOUNDS:  
    print("you need a valid operater (+,-, *, /)")
  else:
    print (result)

  if input("Another calculation (y/n)? ") == "y":
    more_input = True
  else:
    more_input = False

#more_input = True(True if input(Another calculation (y/n)?)== 'y' else False

print ("Bye now")