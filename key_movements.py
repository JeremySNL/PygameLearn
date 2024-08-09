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
        self.right = False
        self.left = False
        self.stepCount = 0
    
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

def redrawScreen():
    man.stepCount
    #Rellena el fondo de la pantalla
    window.blit(bg, (0,0))
    #Dibujar personaje/s
    man.draw(window)
    #Actualizar los movimientos en pantalla
    pygame.display.update()

#Esto nos ayuda a indicar las FPS en el bucle principal
clock = pygame.time.Clock()
run = True
man = player(10, 410, 64, 64)

#Bucle principal
while run:
    #FPS
    clock.tick(27)

    #Bucle de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
        man.left = False
        man.right = False
    #Mecanica de salto
    if not(man.isJumping):
        if keys[pygame.K_SPACE]:
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

    redrawScreen()
#Fin del juego    
pygame.quit()