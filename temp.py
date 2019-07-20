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
        result = -1      
    return result

#print(calculate(1,2,'+'))

first_number = input("What is the first number? ") 
first_number = int(first_number)

second_number = input("What is the second number? ")
second_number = int(second_number)

operater = input("What operation do you want me to do (+,-,*, /)? ")
operater = operater.strip()
  
result = calculate(first_number, second_number, operater)

if result == -1:  
  print("you need a valid operater (+,-, *, /)")
else:
  print (result)

