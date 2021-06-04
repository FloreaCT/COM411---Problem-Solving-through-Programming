class Person: # The class / blueprint for my objects
  #Class Attribute -> Constant, visible to all objects of the class
  MAX_ENERGY = 0
  #Initializer (Special method, invoked only once, at creation)
  def __init__(self, name, age = 0, weight = 10, energy = 100):
    #Instance attributes
    self.name = name
    self.age = age
    self.weight = weight
    if energy > 100:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy
  def hello(self):
    print(f"Hello, my name is {self.name}. I am {self.age} years old and i weight {self.weight} kg. Nice to meet you!")
 
  def grow(self):
    self.age += 1

  def eat(self, food, weight):
    self.weight += weight
    print(f"{self.name} has eaten {food} and now weights {self.weight}")

if __name__ == "__main__":


  Piotr = Person("Piotr", 66, 81, 50)
  Anca = Person("Anca", 18)
  Tim = Person("Tim", weight = 87)

  Anca.hello()
  Tim.hello()
  Piotr.hello()

  Piotr.grow()
  Piotr.hello()

  Tim.eat("Lasagna", 2)
  Tim.hello()
  # print(f"Person 1 has {person1.energy} energy and Person 2 has {person2.energy} energy.")
  # print(f"Person 1 is called {person1.name} and Person 2 is called {person2.name}.")
  # print(person3)