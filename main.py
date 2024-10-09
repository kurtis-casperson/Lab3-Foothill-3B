# Explain what is Polymorphism and provide a code snippet
# Your code snippet must fully function on Repl.it and successfully demonstrate the concept of Polymorphism

# Polymorphism is the ability to use methods with the same names in different classes.  
# This helps with code readability and reusable functionality.  
# In this example both classes need to thave the same information (what model is the car).
# The car_model function can take any object that contains the model method.  
# This allows for both classes to use methods with the same name.

class SUV:
  def model(self):
    print('Toyota 4Runner')

class Sedan:
  def model(self):
    print('Toyota Camry')

def car_model(car):
 return car.model()

SUV_Style = SUV()
Sedan_Style = Sedan()

car_model(SUV_Style)
car_model(Sedan_Style)