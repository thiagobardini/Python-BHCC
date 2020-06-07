

# Name: Thiago Bardini
# CIT125 Python Programming
# Spring 2020
# Project 4: PyGame 


# Based on Simulte by Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, sys, time, pickle, pygame
from pygame.locals import *

FPS = 30

# Width and height of the game window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 175 # Width and Height of each button
BUTTONGAPSIZE = 20 # Distance between each button
TIMEOUT = 4 # seconds before game over if no button is pushed.

# Definition of the colors used by the game
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
# New colors for extra harder buttons
BRIGHTORANGE = (255, 165,   0)
ORANGE       = (255,  69,   0)
BRIGHTPURPLE = (255,   0, 255)
PURPLE       = (128,   0, 128)
BRIGHTBROWN  = (244, 164,  96)
BROWN        = (139,  69,  19)
BRIGHTSALMON = (255, 160, 122)
SALMON       = (240, 128, 128)
# Starting background color
bgColor = BLACK

# New variables created to make it easier to add new buttons
NUMBEROFCOLUMNS = 4
NUMBEROFLINES = 2

XMARGIN = int((WINDOWWIDTH - (NUMBEROFCOLUMNS * BUTTONSIZE) - BUTTONGAPSIZE) / NUMBEROFCOLUMNS)
YMARGIN = int((WINDOWHEIGHT - (NUMBEROFLINES * BUTTONSIZE) - BUTTONGAPSIZE) / NUMBEROFLINES)

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
# Rect objects for the new buttons
ORANGERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
SALMONRECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
PURPLERECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
BROWNRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)



def main():
    # Definition of the global variables for this game
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4, BEEP5, BEEP6, BEEP7, BEEP8

    # Creating the game window
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate Turbo Edition')

    # Drawing the instrctions for the player
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('Match the pattern by clicking on the button or using the Q, W, E, R, A, S, D, F keys.', 1, WHITE)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    # If there is a previous hiscore stored, load it from the file
    try:
        with open('score.txt', 'rb') as file:
            hiscore = pickle.load(file)
    except:
        hiscore = 0

    # load the sound files
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')
    BEEP5 = pygame.mixer.Sound('beep5.ogg')
    BEEP6 = pygame.mixer.Sound('beep6.ogg')
    BEEP7 = pygame.mixer.Sound('beep7.ogg')
    BEEP8 = pygame.mixer.Sound('beep8.ogg')

    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    currentStep = 0 # the color the player must push next
    lastClickTime = 0 # timestamp of the player's last button push
    score = 0
    # when False, the pattern is playing. when True, waiting for the player to click a colored button:
    waitingForInput = False

    while True: # main game loop
    
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, BLUE, ORANGE, BROWN, SALMON, )
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        # Drawing the score on the screen
        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
        
        # Drawing the hiscore on the screen
        hiscoreSurf = BASICFONT.render('Hiscore: ' + str(hiscore), 1, WHITE)
        hiscoreRect = hiscoreSurf.get_rect()
        hiscoreRect.topleft = (10, 10)
        DISPLAYSURF.blit(hiscoreSurf, hiscoreRect)

        DISPLAYSURF.blit(infoSurf, infoRect)

        checkForQuit()
        
        
        for event in pygame.event.get(): # event handling loop
            # If the event was a mouse click, try to determine where the click was
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

            # If the event was pressing a key, try to math it to the corresponding color
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN
                elif event.key == K_d:
                    clickedButton = PURPLE
                elif event.key == K_f:
                    clickedButton = BROWN
                elif event.key == K_e:
                    clickedButton = ORANGE
                elif event.key == K_r:
                    clickedButton = SALMON



        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN, PURPLE, BROWN, ORANGE, SALMON)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # If player score is higher than the high socre, save on file
                if score > hiscore:
                    hiscore = score
                with open('score.txt', 'wb') as file:
                    pickle.dump(hiscore, file)
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

# Makes button flash and play its sound
def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT
    elif color == ORANGE:
        sound = BEEP5
        flashColor = BRIGHTORANGE
        rectangle = ORANGERECT
    elif color == SALMON:
        sound = BEEP6
        flashColor = BRIGHTSALMON
        rectangle = SALMONRECT
    elif color == PURPLE:
        sound = BEEP7
        flashColor = BRIGHTPURPLE
        rectangle = PURPLERECT
    elif color == BROWN:
        sound = BEEP8
        flashColor = BRIGHTBROWN
        rectangle = BROWNRECT
    

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))

# Draws the rectangle of each button
def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)
    pygame.draw.rect(DISPLAYSURF, ORANGE,  ORANGERECT)
    pygame.draw.rect(DISPLAYSURF, SALMON,  SALMONRECT)
    pygame.draw.rect(DISPLAYSURF, PURPLE,  PURPLERECT)
    pygame.draw.rect(DISPLAYSURF, BROWN,  BROWNRECT)


# Changes the background color
def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed): # animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons() # redraw the buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor


def gameOverAnimation(color=WHITE, animationSpeed=50):
    
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play() # play all eight beeps at the same time, roughly.
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    BEEP5.play()
    BEEP6.play()
    BEEP7.play()
    BEEP8.play()
    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)


# This function detects if the coordinates that were sent match with any of the colored buttons
def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint( (x, y) ):
        return YELLOW
    elif BLUERECT.collidepoint( (x, y) ):
        return BLUE
    elif REDRECT.collidepoint( (x, y) ):
        return RED
    elif GREENRECT.collidepoint( (x, y) ):
        return GREEN
    elif ORANGERECT.collidepoint( (x, y) ):
        return ORANGE
    elif SALMONRECT.collidepoint( (x, y) ):
        return SALMON
    elif BROWNRECT.collidepoint( (x, y) ):
        return BROWN
    elif PURPLERECT.collidepoint( (x, y) ):
        return PURPLE    
    return None


if __name__ == '__main__':
    main()
