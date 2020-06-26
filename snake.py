import pygame
import time
import random
import sys

pygame.init()

WIDTH = 800  # 40 części
HEIGHT = 600  # 30 części

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

snakeImg = pygame.image.load('snake.png')
snakeImg = pygame.transform.scale(snakeImg, (20, 20))

fruitImg = pygame.image.load('apple.png')
fruitImg = pygame.transform.scale(fruitImg, (20, 20))


def statement(text):
    font = pygame.font.SysFont("Sans", 115)
    text = font.render(str(text), True, white)
    gameDisplay.blit(text, (200, HEIGHT/2-60))
    pygame.display.update()
    pygame.time.delay(2000)
    game_loop()


def snake(x, y):
    gameDisplay.blit(snakeImg, (x, y))


def snake2(x, y, length):
    for i in range(1, length+1):
        gameDisplay.blit(snakeImg, (x[-i], y[-i]))


def generateFruit():
    xFruit = 20*random.randint(0, 39)
    yFruit = 20*random.randint(0, 29)
    return xFruit, yFruit


def fruit(x, y):
    gameDisplay.blit(fruitImg, (x, y))


def game_loop():
    x = (WIDTH * 0.45)  # 360
    y = (HEIGHT * 0.8)  # 480

    xFruit, yFruit = generateFruit()

    x_change = 0
    y_change = -20

    SnakeTailX = [0, 360, 360]
    SnakeTailY = [0, 500, 480]

    count = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != 20:
                    x_change = -20
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -20:
                    x_change = 20
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != 20:
                    y_change = -20
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change != -20:
                    y_change = 20
                    x_change = 0

        x += x_change
        y += y_change

        SnakeTailX.append(x)
        SnakeTailY.append(y)

        if len(SnakeTailX) >= 151:
            SnakeTailX = SnakeTailX[30:]
            SnakeTailY = SnakeTailY[30:]

        if x > WIDTH - 20 or x < 0 or y > HEIGHT - 20 or y < 0:
            statement("You Lost!")

        for i in range(2, count + 2):
            if SnakeTailX[-1] == SnakeTailX[-i] and SnakeTailY[-1] == SnakeTailY[-i]:
                statement("You Lost!")

        if x == xFruit and y == yFruit:
            count += 2
            xFruit, yFruit = generateFruit()

        gameDisplay.fill(black)
        snake2(SnakeTailX, SnakeTailY, count)
        fruit(xFruit, yFruit)
        pygame.display.update()
        clock.tick(15)


game_loop()
pygame.quit()
quit()
