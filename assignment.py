#-----------------------------------------------------------------------------
# Program Name: Assignment Template (assignment.py)
# Purpose:     <Jumpy Jungle is a side-scrolling platformer game where the player controls a character who must avoid obstacles and collect power-ups as they run through a jungle.
# The game features various game states including a start screen, help screen, pause screen, and game over screen.
# The player must jump over obstacles, collect power-ups, and earn points to increase their score.
# The game is designed using Pygame, and includes features such as sound effects, music, and sprite animations.>
# Author:      <Zaviar>
# Created:     08/04/2023
# Updated:     26/04/2023
#-----------------------------------------------------------------------------
#This project deserves a level 4+ as it demonstrates a clear understanding of the Pygame library and its functions.
# The code includes initialization of the library, setting up the game window and character, loading and resizing sprites, playing background music and sound effects, setting up game states, displaying screens, and handling events.
# Additionally, the code is well organized and uses descriptive variable names, making it easy to read and understand.
# The project also includes features such as scrolling backgrounds, power-ups, and game score tracking, adding to its complexity and demonstrating my skills in programming with Pygame.
# Overall, this project showcases a strong foundation in Pygame and the ability to create functional and engaging games.
    #List of level 3 expectations completed:
# The game must keep a score, timer or have lives using a variable
# The game should have an end and start screen and a menu system to move between screens without having to restart the program.
# The game should have clear instructions on how to play.
# The game must have music and sounds.
# The game uses images
# The game must have a custom downloaded font
# Organized code (indenting and naming conventions)
# Coding decisions should make sense and not include grossly inefficient code.
# The game must have collision detection
# The game has animation (images or shapes moving on the screen using variables).
# The game uses user events (keyboard or mouse input from the user)
# Consistent coding history using github commits (daily or more)
    #List of level 3 expectations missed:
#
    #Features Added Above Level 3 Expectations:
# Powerups with collision detection and effects of powerup
# Increasing difficulty within intervals of five seconds
# Multiple maps with similar game mechanics and objective
# Both obstacle and characters are animated while maintaining collision detection
# Very detailed and illustrated graphics and fonts matching the overall theme of the game

import pygame

#*********SETUP**********
pygame.init()

# Setting variables to set the size of the window
windowWidth = 1280
windowHeight = 720

# Creating the game window
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Jumpy Jungle")

# Setting variables for the game character
character_x = 0
character_y = 615
character_initial_y = 615
character_width = 50
character_height = 50
character_speed = 5
current_sprite = 0
current_sprite2 = 0
sprite_change_speed = 50
time_since_last_sprite_change = 0
character_jump_speed = 10
character_initial_jump_speed = -10
character_jump_height = 100
character_jump_count = 0
character_gravity = 0.6
character_is_jumping = False
character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

# Initializing the game score
score = 0
score_font = pygame.font.SysFont("centurygothicms", 30)

# Setting variables for the game obstacle
obstacle_x = 1280
obstacle_y = 595
obstacle_width = 50
obstacle_height = 50
obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
obstacle_speed = 8

# Initializing Pygame mixer for playing sounds
pygame.mixer.init()

# Loading game music
pygame.mixer.music.load("music.mp3")

# Loading game sound effects
click_sound = pygame.mixer.Sound("click.wav")
obstacle_sound = pygame.mixer.Sound("obstacle.wav")
walk_sound = pygame.mixer.Sound("walk.wav")
die_sound = pygame.mixer.Sound("Powerdown.wav")
gapple_sound = pygame.mixer.Sound("gapple.wav")

# Setting volume for game sounds
pygame.mixer.music.set_volume(0.4)
click_sound_volume = 2.0
obstacle_sound_volume = 0.6
walk_sound_volume = 0.3
click_sound.set_volume(2.0)
obstacle_sound.set_volume(0.6)
walk_sound.set_volume(0.3)

# Starting game music
pygame.mixer.music.play(-1)

# Loading character sprites
character_sprites = [pygame.image.load("run (1).png"),
                     pygame.image.load("run (2).png"),
                     pygame.image.load("run (3).png"),
                     pygame.image.load("run (4).png"),
                     pygame.image.load("run (5).png"),
                     pygame.image.load("run (6).png"),
                     pygame.image.load("run (7).png"),
                     pygame.image.load("run (8).png")]

# Loading obstacle sprites
obstacle_sprites = [pygame.image.load("opp2.png"),
                     pygame.image.load("opp3.png"),
                     pygame.image.load("opp4.png"),
                     pygame.image.load("opp5.png"),
                     pygame.image.load("opp6.png"),]

# Loading powerup sprites
powerup = pygame.image.load("gapple.png")
powerup_x = 1280
powerup_y = 660
powerup_width = 50
powerup_height = 50
powerup_rect = pygame.Rect(powerup_x, powerup_y, powerup_width, powerup_height)
powerup_speed = 5
last_powerup_time = pygame.time.get_ticks()

# Resize character sprites
for i in range(len(character_sprites)):
    character_sprites[i] = pygame.transform.scale(character_sprites[i], (character_sprites[i].get_width() // 5, character_sprites[i].get_height() // 5))

# Resize obstacle sprites
for i in range(len(obstacle_sprites)):
    obstacle_sprites[i] = pygame.transform.scale(obstacle_sprites[i], (obstacle_sprites[i].get_width() * 3.75, obstacle_sprites[i].get_height() * 3.75))

# Resize powerup
powerup = pygame.transform.scale(powerup, (60, 60))

# Loading the background images
background = pygame.image.load("background.jpg")
background1 = pygame.image.load("pioxely12.jpg")
background2 = pygame.image.load("bakgroun.png")
background3 = pygame.image.load("pausee.png")
background4 = pygame.image.load("gameover2.png")
background5 = pygame.image.load("helpppp1.png")

# Set up the clock
clock = pygame.time.Clock()

# Initialize the x position variables for scrolling backgrounds
x_pos = 0
x_pos2 = 0
speed = 5

# Import the time module and start timing the game
import time
start_time = time.time()

# Define game states
gamestate_start = 0
gamestate_play = 1
gamestate_play2 = 2
gamestate_help = 3
gamestate_pause = 4
gamestate_end = 5

# Display the start screen
def show_start_screen():
    global game_state
    # Fill the window with black
    window.fill((0,0,0))
    # Display the background image for the start screen
    window.blit(background2, (0, 0))
    # Set up font for buttons
    font = pygame.font.SysFont("forest", 80)
    # Render the play button text
    play_button = font.render("      ", True, (0,0,0))
    # Render the help button text
    help_button = font.render("      ", True, (0,0,0))
    # Set up the play and help button positions
    play_button_rect = play_button.get_rect(center=(windowWidth/2, windowHeight/2 - 50))
    help_button_rect = help_button.get_rect(center=(windowWidth/2, windowHeight/2 + 50))
    # Blit the play and help buttons onto the screen
    window.blit(play_button, play_button_rect)
    window.blit(help_button, help_button_rect)
    # Update the display
    pygame.display.update()
    
    # Check for mouse button click on play and help buttons
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if play_button_rect.collidepoint(mouse_x, mouse_y):
            game_state = gamestate_play
        elif help_button_rect.collidepoint(mouse_x, mouse_y):
            game_state = gamestate_help
    
    # Check for mouse button click on the button for NEW MAP
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if mouse_x < 1108 + 157 and mouse_x > 1108 and mouse_y < 632 + 74 and mouse_y > 632:
            game_state = gamestate_play2

# Display pause screen
def show_pause_screen():
    global game_state
    # Display the pause screen background image
    window.blit(background3, (0, 0))
    # Create the resume button and quit button
    resume_button = score_font.render("         ", True, (0,0,0))
    quit_button = score_font.render("          ", True, (0,0,0))
    # Get the rectangle for each button, and center them on the screen
    resume_button_rect = resume_button.get_rect(center=(windowWidth/2, windowHeight/2 - 50))
    quit_button_rect = quit_button.get_rect(center=(windowWidth/2, windowHeight/2 + 50))
    # Display the resume and quit buttons on the screen
    window.blit(resume_button, resume_button_rect)
    window.blit(quit_button, quit_button_rect)
    # Update the display to show the new button images
    pygame.display.update()
    
     # Check for mouse button click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        # If the resume button is clicked, set the game state to gamestate_play
        if resume_button_rect.collidepoint(mouse_x, mouse_y):
            game_state = gamestate_play
        # If the quit button is clicked, exit the game
        elif quit_button_rect.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            
# Display the end screen\game over screen
def show_end_screen():
    global game_state
    # Display the end screen background image
    window.blit(background4, (0, 0))
    # Create the score text using the score font
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    # Display the score text on the screen
    window.blit(score_text, (600, 220))
    # Create the play button and quit button using the score font
    play_button = score_font.render("          ", True, (0,0,0))
    quit_button = score_font.render("          ", True, (0,0,0))
    # Get the rectangle for each button, and center them on the screen
    play_button_rect = play_button.get_rect(center=(windowWidth/2, windowHeight/2 - 50))
    quit_button_rect = quit_button.get_rect(center=(windowWidth/2, windowHeight/2 + 50))
    # Display the play and quit buttons on the screen
    window.blit(play_button, play_button_rect)
    window.blit(quit_button, quit_button_rect)
    # Update the display to show the new button images
    pygame.display.update()
    
    # Check for mouse button click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        # If the play button is clicked, set the game state to gamestate_play
        if play_button_rect.collidepoint(mouse_x, mouse_y):
            game_state = gamestate_play
        # If the quit button is clicked, exit the game
        elif quit_button_rect.collidepoint(mouse_x, mouse_y):
            pygame.quit()
    
    # Reset obstacle variables
    # Set obstacle x and y positions to the right of the screen
    global obstacle_x, obstacle_y
    obstacle_x = 1280
    obstacle_y = 595
    
    # Set power-up x and y positions to the right of the screen
    global powerup_x, powerup_y
    powerup_x = 1280
    powerup_y = 660

# Display the game guide/help screen
def show_help_screen():
    # Set the background image to the guide/help screen
    window.blit(background5, (0, 0))
    pygame.display.update()
    
    # Get the position of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        # If the back button is clicked, set the game state to gamestate_start
        if mouse_x < 1108 + 157 and mouse_x > 1108 and mouse_y < 632 + 74 and mouse_y > 632:
            game_state = gamestate_start
            print(game_state)

game_over = False
game_state = gamestate_start

#*********GAME LOOP**********
while True:
    # Loop through all the events in pygame
    for event in pygame.event.get():
        # Check if the user clicks the close button
        if event.type == pygame.QUIT:
            running = False
        # Check if the user presses the escape key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = gamestate_pause
        # Check if the user clicks the left mouse button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_sound.play()
    
    # Check if the game state is play
    if game_state == gamestate_play:
        # Get the elapsed time since the game started
        elapsed_time = time.time() - start_time
        
         # Increase the speed of the game after 5 seconds
        if elapsed_time >= 5:
            speed += 1
            obstacle_speed += 1
            start_time = time.time()
            
        # Move the background image to the left
        x_pos -= speed

        # Wrap the background image around the screen
        if x_pos <= -background.get_width():
            x_pos = 0

        # Draw the background image twice to cover the entire screen
        window.blit(background, (x_pos, 0))
        window.blit(background, (x_pos + background.get_width(), 0))
        
        # Check for space bar input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not character_is_jumping:
                # If the space bar is pressed, set the character to jump
                character_is_jumping = True
                character_jump_count = 0
                character_y -= 1

        # Update character position
        if character_is_jumping:
            # Update jump velocity due to gravity
            character_jump_speed += character_gravity
            # Update character position using jump velocity
            character_y += character_jump_speed
            
            # Check for landing on ground
            if character_y >= character_initial_y:
                # Set character to ground level and stop jumping
                character_y = character_initial_y
                character_is_jumping = False
                character_jump_speed = -15
            else:
                # Move character horizontally
                character_rect.x += character_speed
            
            # Reset jump speed when on the ground
            if character_y == 450:
                character_jump_speed = character_initial_jump_speed
            
            # Play walk sound when not jumping
            if character_is_jumping == False:
                walk_sound.play()
                
        # Update the current sprite
        time_since_last_sprite_change += clock.get_time()
        if time_since_last_sprite_change > sprite_change_speed:
            current_sprite += 1
            if current_sprite >= len(character_sprites):
                current_sprite = 0
            time_since_last_sprite_change = 0

        # Draw the current sprite
        if current_sprite >= len(character_sprites):
            current_sprite = 0
        window.blit(character_sprites[current_sprite], (character_x, character_y))
    
        # Draw powerup
        window.blit(powerup, (powerup_x, powerup_y))
        
        # Move powerup with the background
        powerup_x = powerup_x - powerup_speed #Makes obstacle move with background
    
        # Reset powerup position when off screen
        if powerup_x < -6000:
            powerup_x = windowWidth
        
        # Move obstacle with the background
        obstacle_x = obstacle_x - obstacle_speed
        
        # Reset obstacle position when off screen
        if obstacle_x < -89:
            obstacle_x=1280
        
        # Play sound when obstacle moves off screen
        if obstacle_x == 1280:
            obstacle_sound.play()
            
        # Update the current sprite
        time_since_last_sprite_change += clock.get_time()
        if time_since_last_sprite_change > sprite_change_speed:
            current_sprite2 += 1
            if current_sprite2 >= len(obstacle_sprites):
                current_sprite2 = 0
            time_since_last_sprite_change = 0

        # Draw the current sprite
        if current_sprite2 >= len(obstacle_sprites):
            current_sprite2 = 0
        
        #Draw obstacle
        window.blit(obstacle_sprites[current_sprite2], (obstacle_x, obstacle_y))

        # Check for collisions between character and obstacles/powerups
        character_rect = pygame.Rect(character_x, character_y, 50, 70)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 70)
        powerup_rect = pygame.Rect(powerup_x, powerup_y, 50, 50)
        
        # Handle collision with obstacle
        if character_rect.colliderect(obstacle_rect):
            die_sound.play()
            game_state = gamestate_end
        
        # Handle collision with powerup
        elif character_rect.colliderect(powerup_rect):
            gapple_sound.play()
            if character_rect.colliderect(powerup_rect):
                # Move character up and increase size
                character_y -= 20
                character_initial_y -= 20
                for i in range(len(character_sprites)):
                    character_sprites[i] = pygame.transform.scale(character_sprites[i], (character_sprites[i].get_width() * 1.2, character_sprites[i].get_height() * 1.2))
                
        # Update score every 5 obstacle movements
        if obstacle_x % 5 == 0:
            score += 1
        
        # Display score
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
        # Draw the text at the top-left corner of the screen
        window.blit(score_text, (10, 10))
        
        # Display escape to pause
        score_text = score_font.render("Press ESC to pause game", True, (255, 255, 255))
        # Draw the text at the top-left of the screen
        window.blit(score_text, (150,10))
    
        # Display space to jump
        score_text = score_font.render("Press SPACE to jump", True, (255, 255, 255))
        # Draw the text at the top-left of the screen
        window.blit(score_text, (450,10))
        
    # Handle game states
    elif game_state == gamestate_start:
        show_start_screen()
        
    elif game_state == gamestate_pause:
        show_pause_screen()
        
    elif game_state == gamestate_end:
        show_end_screen()
        
    elif game_state == gamestate_help:
        show_help_screen()
        
    elif game_state == gamestate_play2:
        # Get the elapsed time since the game started
        elapsed_time = time.time() - start_time
        
         # Increase the speed of the game after 5 seconds
        if elapsed_time >= 5:
            speed += 1
            obstacle_speed += 1
            start_time = time.time()
            
        # Move the background image to the left
        x_pos -= speed

        # Wrap the background image around the screen
        if x_pos <= -background1.get_width():
            x_pos = 0

        # Draw the background image twice to cover the entire screen
        window.blit(background1, (x_pos, 0))
        window.blit(background1, (x_pos + background1.get_width(), 0))
        
        # Check for space bar input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not character_is_jumping:
                # If the space bar is pressed, set the character to jump
                character_is_jumping = True
                character_jump_count = 0
                character_y -= 1

        # Update character position
        if character_is_jumping:
            # Update jump velocity due to gravity
            character_jump_speed += character_gravity
            # Update character position using jump velocity
            character_y += character_jump_speed
            
            # Check for landing on ground
            if character_y >= character_initial_y:
                # Set character to ground level and stop jumping
                character_y = character_initial_y
                character_is_jumping = False
                character_jump_speed = -15
            else:
                # Move character horizontally
                character_rect.x += character_speed
            
            # Reset jump speed when on the ground
            if character_y == 450:
                character_jump_speed = character_initial_jump_speed
            
            # Play walk sound when not jumping
            if character_is_jumping == False:
                walk_sound.play()
                
        # Update the current sprite
        time_since_last_sprite_change += clock.get_time()
        if time_since_last_sprite_change > sprite_change_speed:
            current_sprite += 1
            if current_sprite >= len(character_sprites):
                current_sprite = 0
            time_since_last_sprite_change = 0

        # Draw the current sprite
        if current_sprite >= len(character_sprites):
            current_sprite = 0
        window.blit(character_sprites[current_sprite], (character_x, character_y))
    
        # Draw powerup
        window.blit(powerup, (powerup_x, powerup_y))
        
        # Move powerup with the background
        powerup_x = powerup_x - powerup_speed #Makes obstacle move with background
    
        # Reset powerup position when off screen
        if powerup_x < -6000:
            powerup_x = windowWidth
        
        # Move obstacle with the background
        obstacle_x = obstacle_x - obstacle_speed
        
        # Reset obstacle position when off screen
        if obstacle_x < -89:
            obstacle_x=1280
        
        # Play sound when obstacle moves off screen
        if obstacle_x == 1280:
            obstacle_sound.play()
            
        # Update the current sprite
        time_since_last_sprite_change += clock.get_time()
        if time_since_last_sprite_change > sprite_change_speed:
            current_sprite2 += 1
            if current_sprite2 >= len(obstacle_sprites):
                current_sprite2 = 0
            time_since_last_sprite_change = 0

        # Draw the current sprite
        if current_sprite2 >= len(obstacle_sprites):
            current_sprite2 = 0
        
        # Draw obstacle
        window.blit(obstacle_sprites[current_sprite2], (obstacle_x, obstacle_y))

        # Check for collisions between character and obstacles/powerups
        character_rect = pygame.Rect(character_x, character_y, 50, 70)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 70)
        powerup_rect = pygame.Rect(powerup_x, powerup_y, 50, 50)
        
        # Handle collision with obstacle
        if character_rect.colliderect(obstacle_rect):
            die_sound.play()
            game_state = gamestate_end
        
        # Handle collision with powerup
        elif character_rect.colliderect(powerup_rect):
            gapple_sound.play()
            if character_rect.colliderect(powerup_rect):
                # Move character up and increase size
                character_y -= 20
                character_initial_y -= 20
                for i in range(len(character_sprites)):
                    character_sprites[i] = pygame.transform.scale(character_sprites[i], (character_sprites[i].get_width() * 1.2, character_sprites[i].get_height() * 1.2))
                
        # Update score every 5 obstacle movements
        if obstacle_x % 5 == 0:
            score += 1
        
        # Display score
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
        # Draw the score text at the top-left corner of the screen
        window.blit(score_text, (10, 10))

        # Display escape to pause
        score_text = score_font.render("Press ESC to pause game", True, (255, 255, 255))
        # Draw the text at the top-left of the screen
        window.blit(score_text, (120,10))
        
    # Update the screen with all the changes made in this frame
    pygame.display.flip()
    # Wait until the next frame running at 60fps
    clock.tick(60)

pygame.quit()