import pygame as pg
import sys
import random
import time
def player_spaceship():
    global spaceship_x,spaceship_y
    screen.blit(spaceship,(spaceship_x,spaceship_y))
def player_spaceship_measurements():
    global spaceship_x,spaceship_y,screen_width,screen_height,spaceship_width
    if spaceship_x <= 0:
        spaceship_x = 0
    if spaceship_x >= screen_width-spaceship_width:
        spaceship_x = screen_width-spaceship_width
    if spaceship_y >= screen_height-spaceship_height:
        spaceship_y = screen_height-spaceship_height
    if spaceship_y <= 0:
        spaceship_y = 0
def bullet_animation():
    global spaceship_x,spaceship_y,bullet_time
    if bullet_time == 20:
        bullet_ls.append(bullet.get_rect(bottomleft=(spaceship_x+10,spaceship_y)))
        for bull in bullet_ls:
            bull.y -= 10
            if bull.y <= 10:
                bullet_ls.remove(bull)
        bullet_time = 0
    else:
        bullet_time += 1
    for x in bullet_ls:
        screen.blit(bullet,x)
def enemy_animation():
    global enemy_ls,enemy_time,score
    if enemy_time == 20:
        enemy_ls.append(enemy.get_rect(topleft=(random.randrange(10,900,30),0)))
        for enem in enemy_ls:
            enem.y += 10
            if enem.y >= screen_height-10:
                enemy_ls.remove(enem)
                score -= 1
        enemy_time = 0
    else:
        enemy_time += 1
    for x in enemy_ls:
        screen.blit(enemy,x)
def collision_between_bullet_enemy():
    global enemy_ls,bullet_ls,score
    for x in enemy_ls:
        for y in bullet_ls:
            try:
                if y.colliderect(x):
                    bullet_ls.remove(y)
                    enemy_ls.remove(x)
                    score += 1
            except:
                pass
def collision_between_enemy_player(text):
    global enemy_ls,score,spaceship,score_color,enemy_ls,bullet_ls
    score_text_main = text.format(str(score))
    scoretext = pg.font.Font("freesansbold.ttf",30)
    textsurface = scoretext.render(score_text_main,True,score_color)
    textrect = textsurface.get_rect()
    textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    screen.blit(background,(0,0))
    screen.blit(textsurface,textrect)
    enemy_ls.clear()
    bullet_ls.clear()
    pg.display.update()
    time.sleep(5)
    game_running()
def screen_score_text():
    global score,score_color
    score_text = "score : "+str(score)
    scoretext = pg.font.Font("freesansbold.ttf",20)
    textsurface = scoretext.render(score_text,True,score_color)
    textrect = textsurface.get_rect()
    #textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    textrect.center = (830,30)
    screen.blit(textsurface,textrect)
    pg.display.update()
def game_running():
    #pg.display.set_icon(bullet)
    global score
    score = 0
    global spaceship_x,spaceship_y,spaceship_x_change,spaceship_y_change
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    spaceship_x -= spaceship_x_change
                if event.key == pg.K_RIGHT:
                    spaceship_x += spaceship_x_change
                if event.key == pg.K_UP:
                    spaceship_y -= spaceship_y_change
                if event.key == pg.K_DOWN:
                    spaceship_y += spaceship_y_change
        #measuring spaceship positions
        spaceshiprect = spaceship.get_rect(x=spaceship_x,y=spaceship_y)
        for x in enemy_ls:
            if x.colliderect(spaceshiprect):
                highest_score.append(score)
                text = "Oops! your crashed.Yours Score: {}"
                time.sleep(2)
                collision_between_enemy_player(text)
        if score <= -1:
            text1 = "Oops! your score is less than or equal to {}"
            collision_between_enemy_player(text1)
        player_spaceship_measurements()
        screen.blit(background,(0,0))
        bullet_animation()
        enemy_animation()
        collision_between_bullet_enemy()
        player_spaceship()
        screen_score_text()
        pg.display.update()

pg.init()
pg.mixer.init()
pg.mixer.music.load("song.mp3")
pg.mixer.music.play(-1,0.0)
screen_width = 900
screen_height = 600
spaceship_width = 30
spaceship_height = 30
running = 1
highest_score = [0]
score = 0
score_color = (255,255,255)
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("alien Invasion")
#spaceship image loading and needs
spaceship = pg.image.load("spaceship.png")
spaceship_x = 0
spaceship_y = 500
spaceship_x_change = 30
spaceship_y_change = 30
#background photo
background = pg.image.load("spacee.jpeg")
#bullet_animation
bullet = pg.image.load("bullet.png")
bullet_ls = []
bullet_time = 1
#enemy_animation
enemy = pg.image.load("space-ship.png")
enemy_ls = []
enemy_time = 1
game_running()
