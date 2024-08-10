#importando la libreria Pygame
import pygame

#inicializando pygame
pygame.init()
#Creando la ventana (width, height)
screen_width = 852
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))
#Titulo de la ventana
pygame.display.set_caption("The Game")

#Cargando las imagenes para las animaciones
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#Creando clase
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJumping = False
        self.jumpCount = 10
        self.right = True
        self.left = False
        self.stepCount = 0
        self.hitbox = (self.x + 17, self.y + 10, 30, 55)
    
    def draw(self, window):
        if self.stepCount+1 >= 27:
            self.stepCount = 0

        if self.left:
            window.blit(walkLeft[self.stepCount//3], (self.x, self.y))
            self.stepCount += 1
        elif self.right:
            window.blit(walkRight[self.stepCount//3], (self.x, self.y))
            self.stepCount += 1
        else:
            window.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 10, 30, 55)
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

    def get_hit(self):
        print("man got hit!")

class projectile(object):
    def __init__(self, x, y, rad, color, facing):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.rad)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
    
    def draw(self, window):
        self.move()
        if self.walkCount+1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            window.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y, 32, 60)
        pygame.draw.rect(window, (255,0,0), self.hitbox, 2)
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def get_hit(self):
        print("hit")

def redrawScreen():
    #Rellena el fondo de la pantalla
    window.blit(bg, (0,0))
    #Dibujar personaje/s
    man.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    
    #Actualizar los movimientos en pantalla
    pygame.display.update()

#Esto nos ayuda a indicar las FPS en el bucle principal
clock = pygame.time.Clock()
run = True
man = player(10, 405, 64, 64)
goblin = enemy(100, 410, 64, 64, 100)
bullets = []
shootLoop = 0

#Bucle principal
while run:
    #FPS
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 20:
        shootLoop = 0

    #Bucle de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.rad < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.rad > goblin.hitbox[1]:
            if bullet.x + bullet.rad > goblin.hitbox[0] and bullet.x - bullet.rad < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.get_hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 852 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #Asignando un movimiento en los ejes a las teclas de flecha
    keys = pygame.key.get_pressed()

    #Limitaciones al movimiento añadido con la condicional despues del and
    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < (screen_width - man.width):
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.stepCount = 0
    #Mecanica de salto
    if not(man.isJumping):
        if keys[pygame.K_UP]:
            man.isJumping = True
    else:
        if man.jumpCount >= -10:
            if man.jumpCount >= 0:
                man.y -= (man.jumpCount ** 2) * 0.5
                man.jumpCount -= 1
            else:
                man.y -= (man.jumpCount ** 2) * 0.5 * -1
                man.jumpCount -= 1
        else:
            man.isJumping = False
            man.jumpCount = 10
        
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 10:
            if man.left:
                facing = -1
            elif man.right:
                facing = 1
            bullets.append(projectile((man.x + man.width//2), (man.y + man.height//2), 10, (255,0,0), facing))
            shootLoop = 1

    if man.y < goblin.hitbox[1] + goblin.hitbox[3] and man.y + man.height > goblin.hitbox[1]:
            if man.x + man.width > (goblin.hitbox[0] + 15) and (man.x + 20) < goblin.hitbox[0] + goblin.hitbox[2]:
                man.get_hit()
    redrawScreen()
#Fin del juego    
pygame.quit()