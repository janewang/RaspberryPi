# issuu.com/themagpi
# Fish Game
# By antiloquax and Jaseman

import pygame, random from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([600,400])
pygame.display.set_caption("Fish Game")

music = pygame.mixer.Sound("tune.wav")
music.play(-1)
toy = pygame.mixer.Sound("toy.wav")
burp = pygame.mixer.Sound("burp.wav")

tux = pygame.image.load("arm_linux.png").convert_alpha()
fish = pygame.image.load("fish.png").convert_alpha()

tx=280; ty=180; txd=0; tyd=0
bx=600; by=-15
fx=600; fy=random.randint(0,370)
bkcol=[127,212,255]
lives=3; score=0; run = True;

# Draw the surfaces of Tux, Fish and Ball
tuxsurf = pygame.Surface((60,70))
tuxsurf.fill(bkcol)
tuxsurf.set_colorkey(bkcol)
tuxsurf.blit(tux,[0,0])
fishsurf = pygame.Surface((35,30))
fishsurf.fill(bkcol)
fishsurf.set_colorkey(bkcol)
fishsurf.blit(fish,[0,0])
ballsurf = pygame.Surface((60,60))
ballsurf.fill(bkcol)
ballsurf.set_colorkey(bkcol)
ballsruf.set_alpha(128)
pygame.draw.circle(ballsurf,[255,255,255],[30,30],30)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: txd=-4
            if evenk.key == pygame.K_RIGHT: txd=4
            if event.key == pygame.K_UP: tyd=-4
            if event.key == pygame.K_DOWN: tyd=4
        if event.type == pygame.KEYUP:
            txd=0; tyd=0
    tx+=txd; ty+=tyd
    
    # This part stops Tux from leaving the edges of screen
    if tx<0: tx=0
    if tx>=540: tx=540
    if ty<=0: ty=0
    if ty>=330: ty=330
    
    # Make the ball chase Tux
    if bx>=tx: bx=bx-1
    else: bx=bx+1
    if by>=ty: by=by-1
    else: by=by+1
    fx = fx-4
    if fx<=-10: fx=600; fy=random.randomint(0,370)
    
    # Collision Detection (Tux & Fish, Tux & Ball)
    if fx<=tx+50 and fx>=tx and fy>=ty-30 and fy<=ty+70:
        toy.play(); fx=600;fy=random.randint(0,370); score+=1
    if bx<=tx+40 and bx>=tx-40 and by>=ty-50 and by<ty+60:
        burp.play(); bx=600; by=-15; lives -=1; tx=280; ty=180
    
    screen.fill(bkcol);
    screen.blit(tuxsurf,[tx,ty])
    screen.blit(fishsurf,[fx,fy])
    screen.blit(ballsurf,[bx,by])
    font = pygame.font.Font(None,20)
    text = font.render("Score: "+str(score), 1, (0,0,0))
    screen.blit(text,[5,5])
    text = font.render("Lives: "+str(lives), 1, (0,0,0))
    screen.blit(text,[80,5])
    
    if lives <= 0:
        font = pygame.font.Font(None, 120)
        text = font.render("Game over!", 1, (255,0,0))
        screen.blit(text, [36, 150])
        pygame.display.update();pygame.time.wait(4000)
        lives=3; score=0; tx=280; ty=180
    
    pygame.display.update(); clock.tick(100)

pygame.quit()
    
    
#Python version 2.6.6
#Pygame version 1.9.2a0
#OS Debian 6