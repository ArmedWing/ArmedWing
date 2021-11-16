import random
import os
os.system('cls||clear')

print("Hello there! There are 5 races, you must choose one and fight the enemy.\nElf(8atk)\nHuman(6atk)\nOrc(6atk)\nDwarf(5atk)\nTreant(4atk)")

class Race:
    instances = []
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        __class__.instances.append(self) 
### Creating child classes for the Races
class Elf(Race):
    pass

class Orc(Race):
    pass

class Dwarf(Race):
    pass

class Human(Race):
    pass

class Treant(Race):
    pass
### Giving the races attributes
elf = Elf("Elf", 8)
orc = Orc("Orc", 6)
dwarf = Dwarf("Dwarf", 5)
human = Human("Human", 6)
treant = Treant("Treant", 4)

while True:                                        #### While loop to check the user's character selection and print its name and attack
    Character = input("\nChoose a race: ")
    if Character == "Elf":
        Character = elf
        print("You have selected the Elf, it has 8 attack")
        break
    if Character == "Orc":
        Character = orc
        print("You have selected the Orc, it has 6 attack")
        break
    if Character == "Dwarf":
        Character = dwarf
        print("You have selected the Dwarf, it has 5 attack")
        break
    if Character == "Human":
        Character = human
        print("You have selected the Human, it has 6 attack")
        break
    if Character == "Treant":
        Character = treant
        print("You have selected the Treant, it has 4 attack")
        break
    else:
        print("Please select a valid race.")
        continue

randIndex = random.randrange(len(Race.instances))
randPlayerCharacter = Race.instances[randIndex]       ### Selects a random Race

print("Computer has selected", randPlayerCharacter.name, "It has", randPlayerCharacter.attack, "attack")  ### Prints the random selected Race's name and attack

if Character.attack > randPlayerCharacter.attack:           ### Checks if the User input's Character attack is higher than the Computer's random one
    print("You win")
elif Character.attack == randPlayerCharacter.attack:        ### Checks if the User input's Character attack is equal to the Computer's random one
    print("It is a draw!")
else:
    print("You lose")




        













