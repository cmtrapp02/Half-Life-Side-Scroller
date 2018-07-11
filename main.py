import pygame, os.path
from pygame.locals import *

import constants

#player class
class Player(pygame.sprite.Sprite):
    
    speed = 5
    #initialize the player
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.i = img
        self.image = pygame.image.load(self.i)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.facing = 1

    #move the player
    def move(self, direction, pos_y):
        
        self.facing = direction
        self.rect.move_ip(direction * self.speed, pos_y * self.speed)
        #self.rect.top = 100
        
        
class Rects(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.i = img
        self.image = pygame.image.load(self.i)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        

    def update(self, x, y):

        self.rect.x = x
        self.rect.y = y


def detect_collision(player, blocking_group, sprites):

    sprite_collide = pygame.sprite.spritecollide(player, blocking_group, False)
    if sprite_collide:

            index = 0
            for index in range(0, len(sprites)):

                offset_x = player.rect[0] - sprites[index].rect[0]
                offset_y = player.rect[1] - sprites[index].rect[1]

                overlap_area = player.mask.overlap_area(sprites[index].mask, (offset_x, offset_y))

                if overlap_area:
                    index += 1

                    if offset_x >= 1:
                        return 1
                    if offset_x <= -1:
                        return -1
                    if offset_y >= 1:
                        print(offset_y)
                    if offset_y <= -1:
                        print(offset_y)


def player_input(player, collision):

    pressed = pygame.key.get_pressed()
    
    direction = 0
    pos_y = 0
    if pressed[K_a]:
        direction += -1
        if collision == 1:
            direction = 0
    if pressed[K_d]:
        direction += 1
        if collision == -1:
            direction = 0
    if pressed[K_w]:
        pos_y += -1
    if pressed[K_s]:
        pos_y += 1

    player.move(direction, pos_y)


def apply_gravity(pos_y):

    #TODO: apply gravity
    gravity = constants.game.GRAVITY
    pos_y += gravity

 #main function for calling other functions       
def main(winstyle = 0):
    #initialize pygame
    pygame.init()

    #initialize display variables
    winstyle = 1 # toggle fullscreen
    surface = pygame.display.set_mode(constants.game.SCREENRECT.size, pygame.SRCALPHA)
    surface.fill(constants.colors.BLUE)
    pygame.display.flip()

    #initialize clock variables
    clock = pygame.time.Clock()

    #game images
    player_image = 'data/testplayer.png'
    rect_image = 'data/bluetestrect.png'
    rect_image2 = 'data/redtestrect.png'
    rect_image3 = 'data/glaucousbluerect.png'
    background_image = 'data/testbackground.png'
    ground_image = 'data/testrectground.png'
    
    #initialize game classes
    player = Player(player_image)
    #test_rect = Rects(rect_image)
    #test_rect2 = Rects(rect_image2)
    test_rect3 = Rects(rect_image3)
    test_background = Rects(background_image)
    test_ground = Rects(ground_image)

    #update the rect locations
    #test_rect.update(100, 225)
    #test_rect2.update(400, 225)
    test_rect3.update(200, 100)
    test_background.update(0, 0)
    test_ground.update(0, 300)

    #sprite groups
    player_group = pygame.sprite.Group(player)
    blocking_group = pygame.sprite.Group(test_rect3)
    background_group = pygame.sprite.Group(test_background)

    #sprite layers
    #layer_player = pygame.sprite.LayeredUpdates().get_layer_of_sprite(player)
    #layer_rect = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_rect)
    #layer_background = pygame.sprite.LayeredUpdates().get_layer_of_sprite(test_background)

    print(player.mask.get_size())
    print(test_rect3.mask.get_size())

    iii = 0

    all = pygame.sprite.RenderUpdates(background_group, blocking_group, player_group)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        get_size = player.mask.get_size()
        get_at = player.mask.get_at((0,0))
        set_at = player.mask.set_at((0,0))
        
        sprites = [test_rect3]

        if player.rect.colliderect(test_rect3.rect):
            print('collision' + str(iii))
            iii += 1
        
        #handle player inputs and collision
        collision = detect_collision(player, blocking_group, sprites)
        player_input(player, collision)

        #draw the scene
        dirty = all.draw(surface)
        pygame.display.update(dirty)

        #output the fps to the commandline
        display_fps = clock.get_fps()
        #print(display_fps)

        #TODO: fix timestep
        #Cap the frame rate at 40 TEMPORARY
        clock.tick(40)
        
        

    pygame.time.wait(1000)

main()