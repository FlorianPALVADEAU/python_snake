import pygame
from snake import Snake
from fruit import Fruit
from text import Text
from screen import Screen
from sounds import Sounds

pygame.init()

# Setting game window parameters
screen = Screen(1000, "Snake Game by Florian", 50, 0, 70)
timeSet = pygame.time.Clock()

# Setting snake parameters
snake = Snake(screen.tileSet, 1, (0, 0), screen.get_random_position())

# Setting fruit parameters
fruit = Fruit(snake.snake.copy(), screen.get_random_position())
fruit2 = Fruit(snake.snake.copy(), screen.get_random_position())

# Setting score
score = Text(snake.length-1, (screen.mainWindowSize // 2.2, 20))

def eatFruit():
    snake.length += 1
    score.score +=1
    score.DisplayScore(screen.screen)
    Sounds.PlaySound('apple_sound', 'apple_sound')

counter = 0


# Setting Playability to true
game_over = False

# Main loop
while True:
    while game_over == True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_SPACE:
                    snake = Snake(screen.tileSet, 1, (0, 0), screen.get_random_position())
                    fruit = Fruit(snake.snake.copy(), screen.get_random_position())
                    snake.snake.center = screen.get_random_position()
                    fruit.fruit.center = screen.get_random_position()
                    fruit2.fruit.center = screen.get_random_position()
                    score.score = 0
                    game_over = False
    
    # Sounds.PlayMusic('background_music', 'background_music')
    screen.screen.fill((50, 205, 50))
    score.DisplayScore(screen.screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # movements
        if event.type == pygame.KEYDOWN:
            snake.GetMovement(event.key, screen.tileSet)

    # check collisions
    auto_collide = pygame.Rect.collidelist(snake.snake, snake.part[:-1]) != -1
    if snake.snake.left < 0 or snake.snake.right > screen.mainWindowSize or snake.snake.top < 0 or snake.snake.bottom > screen.mainWindowSize or auto_collide:
        game_over = True
        screen.screen.fill(((220,20,60)))
        snake.direction = (0, 0)
        snake.part = [snake.snake.copy()]
        snake.snake.center, fruit.fruit.center, fruit2.fruit.center = (1000000, 0), (10000000, 0), (100000000, 0)
        Text.DisplayLooseMessage(screen.screen, screen.screen, score.score)
        Sounds.PlaySound("loose_sound", "loose_sound")

        
    # check poosition of fruit and snake
    if snake.snake.center == fruit.fruit.center:
        fruit.fruit.center = screen.get_random_position()
        eatFruit()
    elif fruit2 and snake.snake.center == fruit2.fruit.center:
        fruit2.fruit.center = screen.get_random_position()
        eatFruit()

    # draw fruit
    fruit.Draw(screen.screen, 'red', fruit.fruit)
    if score.score >= 7:
        fruit2.Draw(screen.screen, 'red', fruit2.fruit)

    # draw snake
    snake.Draw(screen.screen, snake.part)
    
    # Move snake
    time_now = pygame.time.get_ticks()
    if time_now - screen.time > screen.time_step:
        screen.time = time_now
        snake.snake.move_ip(snake.direction)
        snake.part.append(snake.snake.copy())
        snake.part = snake.part[-snake.length:]
    
    # Adding difficulties depending on player score
    if score.score > 5:
        time_step = 60
    if score.score > 15:
        time_step = 50

    pygame.display.flip()
    timeSet.tick(60)
