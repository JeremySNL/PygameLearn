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

#Variables
red = (0,0,255)
run = True
x = 10
y = 420
width = 40
height = 60
vel = 5
isjumping = False
jumpCount = 10
right = False
left = False
stepCount = 0
clock = pygame.time.Clock()

def redrawScreen():
    global stepCount
    #Rellena el fondo de la pantalla
    window.blit(bg, (0,0))

    if stepCount+1 >= 27:
        stepCount = 0

    if left:
        window.blit(walkLeft[stepCount//3], (x, y))
        stepCount += 1
    elif right:
        window.blit(walkRight[stepCount//3], (x, y))
        stepCount += 1
    else:
        window.blit(char, (x, y))

    #Actualizar los movimientos en pantalla
    pygame.display.update()


#Bucle principal
while run:
    #Incluyendo delay a los eventos para que no vaya tan rapido (x millisengundos de delay)
    #pygame.time.delay(50)
    clock.tick(27)

    #Bucle de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Asignando un movimiento en los ejes a las teclas de flecha
    keys = pygame.key.get_pressed()
    #if pygame.key.get_pressed()[pygame.K_LEFT]:
    #Limitaciones al movimiento añadido con la condicional despues del and
    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < (screen_width - width):
        x += vel
        left = False
        right = True
    else:
        stepCount = 0
        left = False
        right = False
    #Mecanica de salto
    if not(isjumping):
        if keys[pygame.K_SPACE]:
            isjumping = True
    else:
        if jumpCount >= -10:
            if jumpCount >= 0:
                y -= (jumpCount ** 2) * 0.5
                jumpCount -= 1
            else:
                y -= (jumpCount ** 2) * 0.5 * -1
                jumpCount -= 1
        else:
            isjumping = False
            jumpCount = 10

    redrawScreen()
#Fin del juego    
pygame.quit()