#importando la libreria Pygame
import pygame

#inicializando pygame
pygame.init()
#Creando la ventana (width, height)
window = pygame.display.set_mode((500, 500))
#Titulo de la ventana
pygame.display.set_caption("The Game")

#Variables
red = (0,0,255)
run = True
x = 230
y = 220
width = 40
height = 60

#Bucle principal
while run:
    #Incluyendo delay a los eventos para que no vaya tan rapido (100 millisengundos de delay)
    pygame.time.delay(100)

    #Bucle de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Asignando un movimiento en los ejes a las teclas de flecha
    keys = pygame.key.get_pressed()
    #if pygame.key.get_pressed()[pygame.K_LEFT]:
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
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