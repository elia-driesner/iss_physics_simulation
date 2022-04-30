import pygame, sys
import math


WN_SIZE = (900, 900)
WINDOW = pygame.display.set_mode(WN_SIZE)

wn = pygame.Surface(WN_SIZE)

FPS = 90
clock = pygame.time.Clock()

pixel_meter = 12742000 / 150 # 150 pixels = earth width
pixel_meter = pixel_meter / 150

class Object:
    def __init__(self, x, y, height, width, mass, color, image = 0):
        self.mass = mass      
        self.width = width
        self.height = height      
        self.x, self.y = x, y
        self.color = color
        
        self.center = (self.x - self.width / 2, self.y - self.height / 2)
        
        self.start_x = x
        self.start_y = y
        self.start_image = image
        
        self.render = (self.x, self.y)
        
        if image != 0:
            self.image = pygame.transform.scale(image, (self.width, self.height))
            
            self.img_x = self.x
            self.img_y = self.y
            
def calc_gravity(o1, o2):
    r = ((o1.center[0] + o2.center[0]) - (o1.center[1] + o2.center[1])) * pixel_meter
    F = ((6.67428 * 10e-11) * o1.mass * o2.mass) / (r * r)
    print(F)
    
scale = 1000
dest = 0

earth = Object(WN_SIZE[0] / 2, WN_SIZE[1] / 2, 150, 150, 5.972 * 10e24, (0, 0, 255), pygame.image.load('Earth.png'))
iss = Object(earth.center[0] - (pixel_meter / 420000), earth.center[1] - (pixel_meter / 420000), 25, 25, 450 * 1000, (100, 100, 100), pygame.image.load('Satelite.png'))

def updateScale():
    pass
# calc_gravity(earth, iss)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    clock.tick(FPS)
    pygame.display.set_caption(str(round(clock.get_fps(), 2)) + ' FPS')
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_PLUS]:
        scale += 10
    if keys[pygame.K_MINUS] and scale > 920:
        scale -= 10
    updateScale()
            
    wn.fill((0, 0, 0))
    wn.blit(earth.image, earth.center)
    wn.blit(iss.image, iss.center)
    
    if scale > 900:
        dest = 0 - ((scale - 900) / 2)
        
    WINDOW.blit(pygame.transform.scale(wn, (scale, scale)), (dest, dest))
    
    pygame.display.update()