import pygame
import random
import time
pygame.init()
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
fps = 60
lets_continue = True
score = 0
collision = pygame.mixer.Sound(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\boring_game2\Untitled.mp3")
hit = pygame.mixer.Sound(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\boring_game2\sound.wav")
lets_continue = True
plimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\boring_game2\man.png")
plimg_rect = plimg.get_rect()
plimg_rect.center = (width / 15, height / 2)
stimg = pygame.image.load(R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Pygame\boring_game2\star.png")
stimg_rect = stimg.get_rect()
stimg_rect.center = (width // 0.5, height // 2)
stcoinspeed = 10
life = 5
is_y = False
is_ai = False
was_there = False

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] or key[pygame.K_w]) and plimg_rect.centery > 80:
        plimg_rect.centery -= 10
    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and plimg_rect.centery < height - 40:
        plimg_rect.centery += 10
    elif key[pygame.K_q]:
            if is_ai == True:
                is_ai = False
                is_y = False
            else:
                is_ai = True
    if stimg_rect.midleft[0] - stcoinspeed <= 0 and was_there == False:
        stimg_rect.centerx = 20
        was_there = True
    else:
        stimg_rect.centerx -= stcoinspeed
        was_there = False

    if is_ai == True and is_y == False:
        
        if plimg_rect.centery > stimg_rect.centery + 10:
            plimg_rect.centery -= 10
        elif plimg_rect.centery < stimg_rect.centery - 10:
            plimg_rect.centery += 10
        else:
            is_y = True

    if plimg_rect.colliderect(stimg_rect): 
        stimg_rect.x = width // 0.9
        stimg_rect.y = random.randrange(80, 280, 10)
        score += 1
        collision.play()
        stcoinspeed += 1
        is_y = False

    if stimg_rect.midleft[0] <= 0:
        stimg_rect.x = width // 0.9
        stimg_rect.y = random.randrange(80, 280, 10)
        life -= 1
        hit.play()
        is_y = False
    if life <= 0:
        time.sleep(3)
        lets_continue = False

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 50), (width, 50))
    font = pygame.font.SysFont("impact", 20)
    text = font.render(f"Score: {score} Lives: {life}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = width // 2
    text_rect.centery = 25
    screen.blit(plimg, plimg_rect)
    screen.blit(stimg, stimg_rect)
    screen.blit(text, text_rect)
    pygame.display.update()
    clock.tick(fps)
    


pygame.quit()