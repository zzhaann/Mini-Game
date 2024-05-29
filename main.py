import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 500)) #razmer
pygame.display.set_caption("Zhanek ozinin oiynyn zhasady")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.jpg').convert()  #fon

#player

walk_left = [
     pygame.image.load('images/player_left/playerl1.png').convert_alpha(),
     pygame.image.load('images/player_left/playerl2.png').convert_alpha(),
     pygame.image.load('images/player_left/playerl3.png').convert_alpha(),
     pygame.image.load('images/player_left/playerl4.png').convert_alpha(),]

walk_right = [
     pygame.image.load('images/player_right/playerr1.png').convert_alpha(),
     pygame.image.load('images/player_right/playerr2.png').convert_alpha(),
     pygame.image.load('images/player_right/playerr3.png').convert_alpha(),
     pygame.image.load('images/player_right/playerr4.png').convert_alpha(),]


ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_list_in_game =[]

player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 150  #1 position
player_y = 280

is_jump = False  #sekiru ushin
jump_count = 9

bg_sound = pygame.mixer.Sound('sounds/sound1.mp3') #olen
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 4000)
running = True



while running:

    screen.blit(bg, (bg_x, 0)) #bg zhylzhytu
    screen.blit(bg, (bg_x + 1000, 0))


    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y)) #kvadrat

    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -= 10
            if player_rect.colliderect(el):
                print("You lose!")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))


    #granis'a zhane knopkalarmen zhuru

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 800:
        player_x += player_speed


    if not is_jump: #tekseremiz spaceti baskanyn
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -9:
            if jump_count > 0: #playerdin koterilui
                player_y -= (jump_count ** 2) / 2
            else: #tusui
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else: #process bitken son manderdi kaita zhartamyz
            is_jump = False
            jump_count = 9


#player kimyly
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2  #bg ushin
    if bg_x == -1000:
        bg_x = 0


    pygame.display.update() #okno zhabylmau ushin

    for event in pygame.event.get():  #zhabatyn knopka zhumys isteu ushin
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 300)))


    clock.tick(12) #playerdyn zhyldamdygy