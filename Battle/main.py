from character import Hero,Enemy
from weapon import short_bow,iron_sword
import os

hero = Hero(name='Hero', health = 100)  #Creation of the Hero object
hero.equip(iron_sword)
enemy = Enemy(name='Enemy', health = 100, weapon = short_bow)   #Creation of the enemy object

while True:
    os.system("clear")
    hero.attack(enemy)  #Hero attacking method
    enemy.attack(hero)  #Enemy attacking method

    hero.health_bar.draw()
    enemy.health_bar.draw()

    #if cases to know the winner
    if(hero.health==0 and enemy.health != 0):
        print(f"{hero.name} Lost the battle. {enemy.name} Wins")
        break
    elif(enemy.health==0 and hero.health != 0):
        print(f"{enemy.name} Lost the battle. {hero.name} Wins")
        break
    elif(enemy.health==0 and hero.health == 0):
        print(f"it's a tie between {hero.name} and {enemy.name} ")
        break

    #waiting for user input in order to continue the while loop
    input()
    