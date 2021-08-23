import os.path
import random

p = "\n> "

print("Welcome to the RPG Character Generator!")

race = "undefined"
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0

def decide_race():
    global race
    race = input("What race would you like your character to be? (human, elf, orc)" + p).lower()

    if (race != "human" and race != "elf" and race != "orc"):
        print("Invalid race! Choose either human, elf, or orc.")
        decide_race()

def decide_name():
    global name
    name = input("What would you like to name your character?" + p).lower()

def roll_stats(race):
    global strength, dexterity, constitution, intelligence, wisdom, charisma
    if(race == "human"):
        strength = random.randint(4, 6)
        dexterity = random.randint(4, 6)
        constitution = random.randint(4, 6)
        intelligence = random.randint(4, 6)
        wisdom = random.randint(4, 6)
        charisma = random.randint(4, 6)
    elif(race == "elf"):
        strength = random.randint(4, 6)
        dexterity = random.randint(4, 6)
        constitution = random.randint(4, 6)
        intelligence = random.randint(4, 6)
        wisdom = random.randint(4, 6)
        charisma = random.randint(4, 6)
    elif(race == "orc"):
        strength = random.randint(4, 6)
        dexterity = random.randint(4, 6)
        constitution = random.randint(4, 6)
        intelligence = random.randint(4, 6)
        wisdom = random.randint(4, 6)
        charisma = random.randint(4, 6)

def create_file(f):
    file = open(f, "w")
    file.write(f"{name.capitalize()} the {race.capitalize()}\n\nStrength: {strength}\nDexterity: {dexterity}\nConstitution: {constitution}\nIntelligence: {intelligence}\nWisdom: {wisdom}\nCharisma: {charisma}\n")
    file.close()

def decide_file_path():
    global save_path, file_name
    save_path = input("Choose the path to save your character file (leave blank to be placed in current directory)." + p)

    if(not os.path.isdir(save_path)):
        print("Invalid path! Input a correct path or leave blank to be placed in current directory,")
        decide_file_path()

    file_name = input("Choose a name for your character file." + p)

    complete_name = os.path.join(save_path, file_name+".txt")
    
    return complete_name

decide_race()
roll_stats(race)
decide_name()

print(f"\nYour character named {name.capitalize()} is complete!\n")

complete_file_name = decide_file_path()
create_file(complete_file_name)

print("Done! Your character file has been saved.")