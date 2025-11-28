import random
# Welcome message
print("Oh, yes... Paleblood...")
input()
print("Well, you've come to the right place.")
input()
print("Yharnam is the home of blood ministration.")
input()
print("You need only unravel its mistery.")
input()
print("But, where's an outsider like you to begin.")
input()
print("Easy, with a bit of Yharnam blood of your own...")
input()
print("But first, you'll need a contract...")
input()
name = input("Name your character ---> ")
print(f"Welcome " + name)

past_choice = input("""
Choose your past.

[1] Milquetoast
[2] Lone Survivor
[3] Troubled Childhood
[4] Violent Past
[5] Professional
[6] Military Veteran
[7] Noble Scion
[8] Cruel Fate
[9] Waste of Skin
""")
#life choices
if past_choice == "1":
  print("Your Strength 12", "Your Health points 11")
def __init__(self, name= "Milquetoast", base_health = 11, base_strength =  12):
 self.name=name
 self.strength = base_strength

if past_choice == "2":
  print("Your Strength 11", "Your Health points 14")
def __init__(self, name="Lone Survivor", base_health = 14, base_strength = 11):
 self.name=name
 self.strength = base_strength

if past_choice == "3":
  print("Your Strength 12", "Your Health points 11")
def __init__(self, name = "Troubled Childhood", base_health = 11, base_strength = 12):
 self.name=name
 self.strength = base_strength

if past_choice == "4":
  print("Your Strength 15", "Your Health points 12")
def __init__(self, name = "Violent Past", base_health = 12, base_strength = 15):
 self.name=name
 self.strength = base_strength

if past_choice == "5":
  print("Your Strength 9", "Your Health points 9")
def __init__(self, name = "Professional", base_health = 9, base_strength = 9):
 self.name=name
 self.strength = base_strength

if past_choice == "6":
  print("Your Strength 14", "Your Health points 10")
def __init__(self,name= "Military Veteran", base_health = 10, base_strength = 14):
 self.name=name
 self.strength = base_strength

if past_choice == "7":
  print("Your Strength 9", "Your Health points 7")
def __init__(self, name = "Noble Scion", base_health = 7, base_strength = 9):
 self.name=name
 self.strength = base_strength

if past_choice == "8":
  print("Your Strength 12", "Your Health points 11")
def __init__(self, name = "Cruel Fate", base_health = 11, base_strength = 12):
 self.name=name
 self.strength = base_strength

if past_choice == "9":
  print("Your Strength 10", "Your Health points 10")
def __init__(self, name = "Waste of Skin", base_health = 10, base_strength = 10, lvl=1):
 self.name=name
 self.strength = base_strength
 self.Health_points = hp = base_health
 self.lvl = lvl

#class item
class Item: 
 """Föremål som kan vara i spelarens inventory.
  name:str
  strength_bonus: int"""
 def __init__(self, name: str, strength: int=0, health: int=0):
  self.name=name
  self.strength = strength
  self.health = health
  def __str__(self):
        return f"{self.name} (+{self.strength_bonus} (+{self.health})"


#player items
Crusher =Item("Crusher",strength= 3)
Sword =Item("Sword",strength= 1)
Acid= Item("Acid",strength= 2)
sou =Item("Sou ",strength= 3)
Water_Gun=Item("Water Gun", strength=3)
Intergalactic =Item("Intergalacticaldestroyerofeverything",strength= 7)
Medkit= Item("Medkit",strength= 0, health=6)
Blood_vials= Item("Blood vial", strength= 0, health= 7)

items = [Crusher, Sword, Acid, sou, Water_Gun, Intergalactic]

#Monster names

class Monster:
  def __init__(self, name, hp, strength):
    self.name = name
    self.hp = hp
    self.strength = strength

    def dropitem(self):
      if random.random() < 0.5:
        return random.choice(items)
      return None
     
#PLACEHOLDER HP OCH STRENGTH BYT OM NI VILL
monsters = [
  Monster("Scourge Beast", hp = 10, strength = 10),
  Monster("Maneater Boar", hp = 10, strength = 10),
  Monster("Brainsucker", hp = 10, strength = 10),
  Monster("Winter lantern", hp = 10, strength = 10),
  Monster("Church giant", hp = 10, strength = 10),
  Monster("Hunter", hp = 10, strength = 10),
  Monster("Celestial emisary", hp = 10, strength = 10),
  Monster("Orphan of Kos", hp = 10, strength = 10),
  Monster("One reborn", hp = 10, strength = 10),
  Monster("Goblin", hp = 10, strength = 10)
]
enemy = random.choice(monsters)
print(f"A wild {enemy.name} appears! HP {enemy.hp}, STR {enemy.strength}")

dropped = enemy.drop_item()
if dropped:
  print(f"it dropped a {dropped.name}")
else:
  print(f"it dropped nothing...")
 

#CHESTICHESTIE