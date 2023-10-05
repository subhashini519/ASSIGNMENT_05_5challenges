class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
    
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))

point_instance = Point(num1,num2,num3)
result = point_instance.sq_sum()
print(f"The sum of squares of three nos is {result}")