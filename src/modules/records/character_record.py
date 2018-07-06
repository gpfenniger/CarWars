'''
    Methods:
        + Character(name)
        + Character.add_exp(skill_name, exp)
        + Character.level_skill(skill_name, levels)
        + Character.change_money(amount)
        + Character.change_prestige(amount)
        - Character.create_character()
        - Character.select_starting_skill(remaining_choices)

    Character Properties:
        + name
        + skills
            + name
            + exp
            + level
        + money
        + prestige
        + health
        + max_health
        + lbs

    TODO Method List
        + Character.move(dx, dy)
        + Character.draw( TBD )

    TODO Character Propertes
        + inventory
        + equiped_weapon
        + equiped_armor
        + age
        + x
        + y
        + current_stage
'''

# PROTOTYPE CLASS!!!!!
# This class is still in prototyping
# Meaning it works with the terminal
# But not Kivy yet

class Skill:
    # Private Class for character skills
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.level = 0

class Character:
    # Record Class for storing character information and methods

    # Constructor Method
    # NO ARGS : RETURN { Character OBJECT }
    def __init__(self):
        self.name = "Default Name"
        self.skills = [
            Skill("General Skill Points"), Skill("Area Knowledge"),
            Skill("Climbing"), Skill("Computer Tech"),
            Skill("Cyclist"), Skill("Driver"),
            Skill("Fast Talk"), Skill("Gunner"),
            Skill("Handgunner"), Skill("Luck"),
            Skill("Martial Arts"), Skill("Mechanic"),
            Skill("Paramedic"), Skill("Running"),
            Skill("Security"), Skill("Streetwise")
        ]
        self.money = 0
        self.prestige = 0
        self.skills[0].exp += 30
        self.max_health = 3
        self.health = self.max_health
        self.lbs = 150
        self.create_character()

    # Private Method for initial character creation
    # NO ARGS : NO RETURN
    def create_character(self):
        print("Enter your characters name")
        self.name = input() 
        print("You start the game with 30 general skill points.")
        print("The following are the skills your character has:")
        for skill in self.skills:
            print(skill.name)
        print("It costs 10 points to level up to the first level of a skill")
        print("To go past level 3 of a skill it costs 20 points later")
        print("And to learn the first level of a skill in the future")
        print("It will cost $1000, 3 months and the same 10 skill points.")
        self.select_starting_skill(3)
        print("The character " + self.name + " has been succesfully created!")

    # Private Recursive Method for selecting initial skills
    # ARGS { remaining_choices INT } : NO RETURN
    def select_starting_skill(self, remaining_choices):
        print("You can select " + str(remaining_choices) + " skills still")
        print("Type in the full name of a skill including spaces excluding general skill points")
        selected_skill = input()
        for skill in self.skills:
            if selected_skill == skill.name and skill.name != "General Skill Points":
                skill.level += 1
                remaining_choices -= 1
                if remaining_choices > 0:
                    self.select_starting_skill(remaining_choices)    
                return
        print("That was not a skill choice, please try again")
        self.select_starting_skill(remaining_choices)

    # Public Method for adding exp to a characters skill
    # ARGS { skill_name STRING, exp INT } : NO RETURN
    def add_exp(self, skill_name, exp):
        if exp < 0:
            print("This is not a proper value")
            return
        for skill in self.skills:
            if skill.name == skill_name:
                skill.exp += exp
                return
        print("Please check you entered the skill name correctly")

    # Public Method for leveling up a characters skill
    # ARGS { skill_name STRING, levels INT } : NO RETURN
    def level_skill(self, skill_name, levels):
        # Checks to make sure arguments are valid
        if levels <= 0:
            print("You cannot level a skill by that amount.")
            return
        if skill_name == "General Skill Points":
            print("You cannot level up general skill points.")
            return
        
        # Finds skill and confirms cost with user
        for skill in self.skills:
            if skill_name == skill.name:
                cost = 0
                money_cost = 1000 if skill.level == 0 else 0
                for i in range(levels):
                    cost += (((skill.level + i) // 3) * 10) + 10
                print("This will cost you " + str(cost) + " skill points and $" + str(money_cost))
                print("If you would like to learn this type y.")
                if input() == 'y' and (skill.exp >= cost or (skill.exp + self.skills[0].exp) >= cost):
                    skill.level += 1
                    if skill.exp < cost:
                        self.skills[0].exp -= (cost - skill.exp)
                        skill.exp = 0
                    else:
                        skill.exp -= cost
                else:
                    print("You can't afford it right now")
                return
        print("That is not a skill")

    # Public Method for adding or removing player money
    # ARGS { amount INT } : NO RETURN
    def change_money(self, amount):
        if self.money + amount < 0:
            print("This will bring you into a negative balance.") 
        self.money += amount
        print("Current Balance: $" + str(self.money))

    # Public Method for adding or removing player prestige
    # ARGS { amount INT } : NO RETURN
    def change_prestige(self, amount):
        if self.prestige + amount >= 0:
            self.prestige += amount
        else:
            self.prestige = 0
        print("Your prestige score is " + str(self.prestige) + ".")

    # TODO Method for drawing on canvas
    # TODO Method for moving on canvas