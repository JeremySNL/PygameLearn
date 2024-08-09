#importando la libreria Pygame
import pygame

#inicializando pygame
pygame.init()
#Creando la ventana (width, height)
screen_width = 500
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
#Titulo de la ventana
pygame.display.set_caption("The Game")

#Variables
red = (0,0,255)
run = True
x = 230
y = 220
width = 40
height = 60
vel = 5

isjumping = False
jumpCount = 10

#Bucle principal
while run:
    #Incluyendo delay a los eventos para que no vaya tan rapido (x millisengundos de delay)
    pygame.time.delay(80)

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
    if keys[pygame.K_RIGHT] and x < (screen_width - width):
        x += vel
    #Mecanica de salto
    if not(isjumping):
        if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < (screen_height - height):
            y += vel
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

    #Otra opcion, asignarle movimiento al mouse
    #x, y = pygame.mouse.get_pos()

    #rellenar la pantalla
    window.fill((0,0,0))
    #Dibujar el rectangulo que moveremos por la pantalla
    pygame.draw.rect(window, red, (x, y, width, height))
    #Actualizar los movimientos en pantalla
    pygame.display.update()

#Fin del juego    
pygame.quit()