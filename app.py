import pygame
from pygame.locals import *
import random

# Windows Size
size = width, height = (800, 800)
# road width
road_w = int(width/1.6)
# roadmark width
roadmark_w = int(width/80)
# location parameters
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# car speed
speed = 2

# Initiallize the app
pygame.init()
running = True

# Set windows size
screen = pygame.display.set_mode(size)
# Set title
pygame.display.set_caption("Car Game")
# Set background color
screen.fill((194, 178, 128))

# Apply change
pygame.display.update()

# Load player car
car = pygame.image.load("car.png")
# car location
car_loc =  car.get_rect()
car_loc.center = right_lane, height*0.8

# Load enemy car
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0 
# game loop
while running:
    counter += 1
    # Increase speed
    if counter == 1024:
        speed +=0.25
        counter = 0
        print("level up", speed)

    # animate enemy vehichle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break


    # Event listener 
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # move car to left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            # move car to right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    
    # Draw road graphics
    # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height)
    )
    # Draw center line, yellow
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2-roadmark_w/2, 0, roadmark_w, height)
    )
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
        
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))


    # Place car images on screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # update changes
    pygame.display.update()

# Close applicatiion windows
pygame.quit()