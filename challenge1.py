class Point():
   def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
   def sqsum(self):
    sum = 0
    sum = ((self.x)**2) + ((self.y)**2)+((self.z)**2)
    return sum
x = int(input("enter value of x : "))    
y = int(input("enter value of y : ")) 
z = int(input("enter value of z : ")) 

obj = Point(x,y,z)
print(obj.sqsum())
    


 

