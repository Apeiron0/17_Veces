import sys
import pygame
from pygame.locals import*
pygame.init()
#import doce_mas
import class17Veces
#from archivo import nombre_clase

altura=800
ancho=600

def main():

    pygame.init()
    screen=pygame.display.set_mode((altura,ancho))
    pygame.display.set_caption("17 veces")
    fondo=pygame.image.load("img/fondo.png").convert()


    j1=[0,0,0,0,0,0]
    j2=[0,0,0,0,0,0]
    qw=class17Veces.AgregarCara
    #tj1=pygame.image.load("img/j1.png").convert()
    #tj2=pygame.image.load("img/j2.png").convert()
    tj1="turno jugador #1"
    tj2="turno jugador #2"

    d1=pygame.image.load("img/1.png").convert()
    d2=pygame.image.load("img/2.png").convert()
    d3=pygame.image.load("img/3.png").convert()
    d4=pygame.image.load("img/4.png").convert()
    d5=pygame.image.load("img/5.png").convert()

    teclas=pygame.image.load("img/teclas.png").convert()

    screen.blit(fondo,(0,0))

    turno=2

    while True:
        screen.blit(d1,(350,150))
        screen.blit(d2,(450,150))
        screen.blit(d3,(250,150))
        screen.blit(d4,(350,250))
        screen.blit(d5,(450,250))
        screen.blit(teclas,(20,400))
        for evento in pygame.event.get():
            if evento.type==QUIT:
                sys.exit()
            elif evento.type==KEYUP:
                if evento.key==K_SPACE:
                    dado1=class17Veces.LanzarDado()
                    dado2=class17Veces.LanzarDado()
                    dado3=class17Veces.LanzarDado()
                    dado4=class17Veces.LanzarDado()
                    dado5=class17Veces.LanzarDado()
                    if dado1==1:
                        d1=pygame.image.load("img/1.png").convert()
                    if dado1==2:
                        d1=pygame.image.load("img/2.png").convert()
                    if dado1==3:
                        d1=pygame.image.load("img/3.png").convert()
                    if dado1==4:
                        d1=pygame.image.load("img/4.png").convert()
                    if dado1==5:
                        d1=pygame.image.load("img/5.png").convert()
                    if dado1==6:
                        d1=pygame.image.load("img/6.png").convert()
                        #dado 2
                    if dado2==1:
                        d2=pygame.image.load("img/1.png").convert()
                    if dado2==2:
                        d2=pygame.image.load("img/2.png").convert()
                    if dado2==3:
                        d2=pygame.image.load("img/3.png").convert()
                    if dado2==4:
                        d2=pygame.image.load("img/4.png").convert()
                    if dado2==5:
                        d2=pygame.image.load("img/5.png").convert()
                    if dado2==6:
                        d2=pygame.image.load("img/6.png").convert()

                    if dado3==1:
                        d3=pygame.image.load("img/1.png").convert()
                    if dado3==2:
                        d3=pygame.image.load("img/2.png").convert()
                    if dado3==3:
                        d3=pygame.image.load("img/3.png").convert()
                    if dado3==4:
                        d3=pygame.image.load("img/4.png").convert()
                    if dado3==5:
                        d3=pygame.image.load("img/5.png").convert()
                    if dado3==6:
                        d3=pygame.image.load("img/6.png").convert()

                    if dado4==1:
                        d4=pygame.image.load("img/1.png").convert()
                    if dado4==2:
                        d4=pygame.image.load("img/2.png").convert()
                    if dado4==3:
                        d4=pygame.image.load("img/3.png").convert()
                    if dado4==4:
                        d4=pygame.image.load("img/4.png").convert()
                    if dado4==5:
                        d4=pygame.image.load("img/5.png").convert()
                    if dado4==6:
                        d4=pygame.image.load("img/6.png").convert()

                    if dado5==1:
                        d5=pygame.image.load("img/1.png").convert()
                    if dado5==2:
                        d5=pygame.image.load("img/2.png").convert()
                    if dado5==3:
                        d5=pygame.image.load("img/3.png").convert()
                    if dado5==4:
                        d5=pygame.image.load("img/4.png").convert()
                    if dado5==5:
                        d5=pygame.image.load("img/5.png").convert()
                    if dado5==6:
                        d5=pygame.image.load("img/6.png").convert()
                    turno=turno+1
                if turno%2==0:
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj1,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=250
                    rectanguloTextoPresent.centery=250
                    #juego
                    j1=qw(dado1,*j1)
                else:
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj2,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=250
                    rectanguloTextoPresent.centery=250
                    j2=qw(dado1,*j1)
                screen.blit(imagenTextoPresent,rectanguloTextoPresent)

                #letreros de los jugadores
                p1x=50
                p2x=400
                for er in j1:
                    qw=str(er)
                    letra=pygame.font.SysFont("Arial",30)
                    img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                    r_j1=img_j1.get_rect()
                    r_j1.centerx=p1x
                    p1x=p1x+30
                    r_j1.centery=50
                    screen.blit(img_j1,r_j1)

                for er in j2:
                    qw=str(er)
                    letra=pygame.font.SysFont("Arial",30)
                    img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                    r_j1=img_j1.get_rect()
                    r_j1.centerx=p2x
                    p2x=p2x+30
                    r_j1.centery=50
                    screen.blit(img_j1,r_j1)


        pygame.display.flip()

main()