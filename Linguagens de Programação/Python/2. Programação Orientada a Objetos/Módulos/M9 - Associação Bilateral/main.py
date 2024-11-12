from modules import House, Person

mother = Person('Anne')
mothersHouse = House()

# creating the bilateral association:
mother.setLocal(mothersHouse)
mothersHouse.setOwner(mother)

# the house understands that the owner is Anne:
mothersHouse.getOwner().introduceYourself()

# the person understands that the local is Anne´s house:
print(mother.getLocal().getAddress())