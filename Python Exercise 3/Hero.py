from os import name

# Base weapon class with damage and name attributes
class Weapon:
    def __init__(self, demage, myth):
        self.demage=demage
        self.myth=myth


# Axe weapon subclass
class Axe(Weapon):
    def __init__(self, demage, myth):
        super().__init__(demage, myth)



# Sword weapon subclass
class Sword(Weapon):
    def __init__(self, demage, myth):
        super().__init__(demage, myth)


# Hero class representing a warrior character
class Hero:
    def __init__(self,name,power,weapon):
        self.name=name
        self.power=power
        self.health=100
        self.weapon=weapon

    # Check hero's health status and print message
    def _check_health(self):
        if self.health > 0 :
            print("The war gonna never stop!")
        else:
            print("Hero sarcastically defeated!")

    # Perform attack action, calculate damage and reduce health
    def _attack(self):
        demage=self.power + self.weapon.demage
        self.health-=5
        print(f"The warrior attacked with {self.weapon.myth} and caused {demage} demage!")
        print(f"Fatigue cause u lost 5 hp {self.health}")

# Create hero instance with axe weapon
dwarf=Hero(
    "Dwarf", 67,
        Axe(59,"Axe Of Millenium")
)

# Execute attack sequence
dwarf._attack()
dwarf._attack()
dwarf._attack()


