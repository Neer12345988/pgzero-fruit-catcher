import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Catch the fruit"

fruits = 0
lives = 3
objects = ["fruit", "fruit", "fruit", "fruit", "fruit", "bomb"]
goes = 0
is_game_over = False
f_or_b = True

basket = Actor("basket")
basket.pos = (WIDTH/2, HEIGHT - 40)

def draw():
    screen.blit("bg", (0,0))
    basket.draw()
    if f_or_b == True:
        fruit.draw()
    else:
        bomb.draw()

def update():
    global goes, objects, f_or_b
    while True:
        move_basket()
        if goes % 6 == 0:
            goes = 0
            random.shuffle(objects)
        if objects[goes] == "fruit":
            fruit = Actor("fruit")
            fruit.pos = (random.randint(40, WIDTH - 40), random.randint(0, 100))
            f_or_b = True
        else:
            bomb = Actor("bomb")
            bomb.pos = (random.randint(30, WIDTH - 30), random.randint(60, 100))
            f_or_b = False
        
        if f_or_b == True:
            while fruit.y > basket.y:
                fruit.y += 30
            if fruit.colliderect(basket):
                fruits += 1
                goes += 1
            elif fruit.y >= HEIGHT:
                goes += 1
        
        while f_or_b == False:  
            while bomb.y > basket.y:
                bomb.y += 50
            if bomb.colliderect(basket):
                is_game_over = True
            elif bomb.y >= HEIGHT:
                goes += 1

def move_basket():
    if keyboard.left or keyboard.a:
        basket.x -= 10
    elif keyboard.right or keyboard.d:
        basket.x += 10

# def move_fruit():
#     while fruit.y > basket.y:
#         fruit.y += 30
#     if fruit.colliderect(basket):
#         fruits += 1
#         goes += 1
#     elif fruit.y >= HEIGHT:
#         goes += 1

# def move_bomb():  
#     while bomb.y > basket.y:
#         bomb.y += 50
#     if bomb.colliderect(basket):
#         is_game_over = True
#     elif bomb.y >= HEIGHT:
#         goes += 1


pgzrun.go()