"""
Create a Chicken  class.  Each Chicken has a species  and a name , as well as an integer attribute called eggs .
eggs should always start out at 0.

Each Chicken should also have an instance method called lay_egg() which should increment and
then return that particular Chicken's eggs  attribute. lay_egg()
should also increment a class variable called total_eggs
"""


class Chicken:
    total_eggs=0
    def __init__(self, species,name):
        self.species=species
        self.name=name
        self.eggs = 0
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs +=1
        return self.eggs



c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
print(Chicken.total_eggs) #0
print(c1.lay_egg())  #1
print(Chicken.total_eggs) #1
print(c2.lay_egg())  #1
print(c2.lay_egg())  #2
print(Chicken.total_eggs) #3