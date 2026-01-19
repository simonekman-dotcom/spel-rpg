import random

print("Oh, yes... Paleblood...")
input()
print("You've come to the right place.")
input()
print("Yharnam is the home of blood ministration.")
input()
print("But first, you'll need a contract...")
input()

name = input("Name your character ---> ")
print(f"Welcome, {name}.")

past_choice = input("""
Choose your past:

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

if past_choice == "1":
    base_strength, base_health = 12, 11
elif past_choice == "2":
    base_strength, base_health = 11, 14
elif past_choice == "3":
    base_strength, base_health = 12, 11
elif past_choice == "4":
    base_strength, base_health = 15, 12
elif past_choice == "5":
    base_strength, base_health = 9, 9
elif past_choice == "6":
    base_strength, base_health = 14, 10
elif past_choice == "7":
    base_strength, base_health = 9, 7
elif past_choice == "8":
    base_strength, base_health = 12, 11
elif past_choice == "9":
    base_strength, base_health = 10, 10
else:
    base_strength, base_health = 10, 10

print(f"STR: {base_strength} | HP: {base_health}")


def choose_door_prompt():
    while True:
        choice = input("\nChoose a door: [1] Left  [2] Forward  [3] Right > ")
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid choice.")

class Item:
    def __init__(self, name, strength=0, health=0):
        self.name = name
        self.strength = strength
        self.health = health

    def __str__(self):
        return f"{self.name} (+{self.strength} STR, +{self.health} HP)"


class Player:
    def __init__(self, name, base_strength, hp):
        self.name = name
        self.base_strength = base_strength
        self.hp = hp
        self.level = 1
        self.inventory = []

    def total_strength(self):
        return self.base_strength + sum(item.strength for item in self.inventory)

    def add_item(self, item):
        self.inventory.append(item)
        self.hp += item.health
        print(f"You obtained {item}!")

    def take_damage(self, dmg):
        self.hp -= dmg

    def level_up(self, n):
        self.level += n

    def is_alive(self):
        return self.hp > 0


class Monster:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def drop_item(self):
        if random.random() < 0.5:
            return random.choice(items)
        return None


items = [
    Item("Sword", strength=1),
    Item("Crusher", strength=3),
    Item("Blood Vial", health=5),
    Item("Hunter Axe", strength=2),
    Item("Medkit", health=7)
]

monsters = [
    Monster("Scourge Beast", 10),
    Monster("Hunter", 9),
    Monster("Brainsucker", 8),
    Monster("Goblin", 6),
    Monster("Church Giant", 12)
]


def encounter(player):
    monster = random.choice(monsters)

    print(f"\nA {monster.name} appears!")
    print(f"Monster STR: {monster.strength}")
    print(f"Your STR: {player.total_strength()}")

    if player.total_strength() > monster.strength:
        print("You defeated the monster.")
        player.level_up(1)

        drop = monster.drop_item()
        if drop:
            player.add_item(drop)

    elif player.total_strength() < monster.strength:
        print("The monster was stronger...")
        player.take_damage(1)

    else:
        print("It's a draw. Nothing happens.")

    print(f"HP: {player.hp} | Level: {player.level}")

player = Player(name, base_strength, base_health)

print("\nThe hunt begins...")

while player.is_alive():
    door = choose_door_prompt()

    
    if door in (1, 2, 3):
        if random.random() < 0.7:
            encounter(player)
        else:
            loot = random.choice(items)
            print("\nYou found loot behind the door.")
            player.add_item(loot)

    if player.level >= 10:
        print("\nYou transcended the hunt.")
        print("YOU WIN.")
        break

if not player.is_alive():
    print("\nYou have fallen.")
    print("GAME OVER.")
