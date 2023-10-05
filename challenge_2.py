#  In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.

# Problem statement Write a Python class called Calculator by completing the tasks below:

class Calculator():
   def __init__(self,num1,num2):
      self.num1 = num1
      self.num2 = num2

   def addition(self):
      return self.num1 + self.num2 

   def subtraction(self):
      return self.num1 - self.num2

   def multiplication(self):
      return self.num1 * self.num2

   def division(self):
    return self.num1 / self.num2

num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
Calculator_instance = Calculator(num1,num2)

Addition = Calculator_instance.addition()
Subtraction = Calculator_instance.subtraction()
Multiplication = Calculator_instance.multiplication()
Division = Calculator_instance.division()

print(f"Addition :{Addition:.2f}\nSubtraction : {Subtraction: .2f}\nMultiplication: {Multiplication: .2f}\nDivision : {Division : .2f}")