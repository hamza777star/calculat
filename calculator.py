#Created by Hamza Khan.
while True:
  from math import sin,cos,tan,sqrt
  print("[-]∆/\/\Z∆")
  print("options")
  print("Enter 'add' to add")
  print("Enter 'subtract' to subtract")
  print("Enter 'multiply' to multiply")
  print("Enter 'divide' to divide")
  print("Enter 'percent' to take percentage")
  print("Enter 'function' for trigonometric funtions")
  print("Enter 'root' for square root")
 # print("Enter 'expo' for power")
  
    
  user_input = input(": ")
    
  if user_input == "quite":
     break
     
  elif user_input == "root":
     num1 = float(input("please enter any number :"))
     result = str(sqrt(num1))
     print("square root of entered number is " + result)
     
  elif user_input == "function":
     print("Enter 'cos' for Cos function")
     print("Enter 'sin' for Sin function")
     print("Enter 'tan' for Tan function")
     user_input = input(":")
     
     if user_input == "cos":
        num1 = float(input("please enter angle:"))
        result = str(cos(num1))
        print("the answer is" + result)

     
     if user_input == "tan":
         num1 = float(input("please enter angle:"))
         ans = str(tan(num1))
         print("the anser is" + ans)
         
     if user_input == "sin":
         num1 = float(input("please enter angle:"))
         ans = str(sin(num1))
         print("the answer is" + ans)       
        
  elif user_input == "add":
     num1 = float(input("please enter first number:"))
     num2 = float(input("please enter second number:"))
     result = str(num1 + num2)
     print(" ")
     print("result is " + result)
     
  elif user_input == "subtract":
     num1 = float(input("please enter first number:"))
     num2 = float(input("please enter second number:"))
     result = str(num1 - num2)
     print(" ")
     print("result is " + result)
     
  elif user_input == "multiply":
     num1 = float(input("please enter first number:"))
     num2 = float(input("please enter second number:"))
     result = str(num1 * num2)
     print(" ")
     print("result is " + result)
  
  elif user_input == "divide":
 	   
     num1 = float(input("please enter first number:"))
     num2 = float(input("please enter second number:"))
     result = str(num1 / num2)
     print("first number divided by second number =" +  result)   
 
  elif user_input == "percent":
     num1 = float(input("please enter total numbers:"))
     num2 = float (input("please enter gained numbers:"))
     a = (num2 * 100)
     result = str(a / num1)
     print("percentage=" + result)
      
print("thanks for using my tool")