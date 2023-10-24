# Jackson Harvey, 09/28/2023, CS 135, Calculator

import math

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def sin(a):
  return math.sin(a)

def cos(a):
  return math.cos(a)

def expo(a,b):
  return math.pow(a,b)

def sqrt(a):
  return math.sqrt(a)
  
while True:
   operator = input("<--Enter the operation: +,-,*,/,^,sqrt,cos,sin, or 'q' to quit-->")
   if operator == "q":
     break 
   elif operator == "sin":
     x = float(input("Enter a number: "))
     value = sin(x)
     print(f"{operator}({x}) = {value}")
   elif operator == "cos":
     x = float(input("Enter a number: "))
     value = cos(x)
     print(f"{operator}({x}) = {value}")
   elif operator == "sqrt":
     x = float(input("Enter a number: "))
     value = sqrt(a)
     print(f"{operator}({x}) = {value}")
   else:
     x = float(input("Enter the first number: "))
     y = float(input("Enter the second number: "))

     if operator == "+":
       value = add(x,y)
       print(f"{x} {operator} {y} = {value}")
     elif operator == "-":
       value = sub(x,y)
       print(f"{x} {operator} {y} = {value}")
     elif operator == "*":
       value = mul(x,y)
       print(f"{x} {operator} {y} = {value}")
     elif operator == "/":
       if y == 0:
         print("That's a no-no! Don't put 0 in the denominator.")
         continue
     elif operator == "^":
         value = expo(x,y)
         print(f"{x} {operator} {y} = {value}")
       else:
         value = div(x,y)
         print(f"{x} {operator} {y} = {value}")
     else:
       print("Please enter a valid operation")