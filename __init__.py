import sys
import pygame
from pygame.locals import*
pygame.init()
import class17Veces

altura=800
ancho=600

def main():

    pygame.init()
    screen=pygame.display.set_mode((altura,ancho))
    pygame.display.set_caption("17 veces")
    fondo=pygame.image.load("img/fondo.png").convert()

    turno=1
    j1=[0,0,0,0,0,0]
    j2=[0,0,0,0,0,0]
    tj1="Turno jugador #1"
    tj2="Turno jugador #2"
    gana_j1="El ganador es el jugador #1"
    gana_j2="El ganador es el jugador #2"

    agregar=class17Veces.AgregarCara
    img_dado=class17Veces.dados
    ver_ganador=class17Veces.VerfGanador

    d1=pygame.image.load("img/1.png").convert()
    d2=pygame.image.load("img/2.png").convert()
    d3=pygame.image.load("img/3.png").convert()
    d4=pygame.image.load("img/4.png").convert()
    d5=pygame.image.load("img/5.png").convert()
    teclas=pygame.image.load("img/teclas.png").convert()

    screen.blit(fondo,(0,0))

    while True:
        screen.blit(d1,(350,150))
        screen.blit(d2,(450,150))
        screen.blit(d3,(250,150))
        screen.blit(d4,(350,250))
        screen.blit(d5,(450,250))
        screen.blit(teclas,(400,400))

        for evento in pygame.event.get():

            if evento.type==QUIT:
                sys.exit()

            elif evento.type==KEYUP:
                if evento.key==K_SPACE:
                    turno=turno+1
                    #Lanzar Dados
                    dado1=class17Veces.LanzarDado()
                    dado2=class17Veces.LanzarDado()
                    dado3=class17Veces.LanzarDado()
                    dado4=class17Veces.LanzarDado()
                    dado5=class17Veces.LanzarDado()
                    tirada=[dado1,dado2,dado3,dado4,dado5]
                    if turno%2==0:
                        for x in tirada:
                            j2=agregar(x,*j2)
                            winer=ver_ganador(x,*j2)
                            if winer==True:
                                l30=pygame.font.SysFont("Arial",30)
                                iTP=l30.render(gana_j2,True,(50,50,50),(0,0,0))
                                rTP=iTP.get_rect()
                                rTP.centerx=150
                                rTP.centery=400
                                screen.blit(iTP,rTP)
                        print "este es el arreglo del primer jugador"
                        print tirada
                        print "esto me devuelve el metodo en turno par"
                        print j1
                    else:
                        for x in tirada:
                            j1=agregar(x,*j1)
                            winer=ver_ganador(x,*j2)
                            if winer==True:
                                l30=pygame.font.SysFont("Arial",30)
                                iTP=l30.render(gana_j1,True,(50,50,50),(0,0,0))
                                rTP=iTP.get_rect()
                                rTP.centerx=150
                                rTP.centery=400
                                screen.blit(iTP,rTP)
                        print "este es el arreglo del segundo jugador"
                        print tirada
                        print "esto me devuelve el metodo en turno impar"
                        print j1
                    #Se carga la imagen
                    d1=pygame.image.load(img_dado(dado1)).convert()
                    d2=pygame.image.load(img_dado(dado2)).convert()
                    d3=pygame.image.load(img_dado(dado3)).convert()
                    d4=pygame.image.load(img_dado(dado4)).convert()
                    d5=pygame.image.load(img_dado(dado5)).convert()
                    #Se imprime el letrero correspondiente a quien tiro los dados
            if turno%2==0:
                letra30=pygame.font.SysFont("Arial",20)
                imagenTextoPresent=letra30.render(tj2,True,(50,50,50),(0,0,0))
                rectanguloTextoPresent=imagenTextoPresent.get_rect()
                rectanguloTextoPresent.centerx=150
                rectanguloTextoPresent.centery=300
            else:
                letra30=pygame.font.SysFont("Arial",20)
                imagenTextoPresent=letra30.render(tj1,True,(50,50,50),(0,0,0))
                rectanguloTextoPresent=imagenTextoPresent.get_rect()
                rectanguloTextoPresent.centerx=150
                rectanguloTextoPresent.centery=300
            screen.blit(imagenTextoPresent,rectanguloTextoPresent)

                #Marcador de los jugadores
            p1x=50
            p2x=400
            for er in j1:
                qw=str(er)
                letra=pygame.font.SysFont("Arial",30)
                img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                r_j1=img_j1.get_rect()
                r_j1.centerx=p1x
                p1x=p1x+40
                r_j1.centery=50
                screen.blit(img_j1,r_j1)

            for er in j2:
                qw=str(er)
                letra=pygame.font.SysFont("Arial",30)
                img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                r_j1=img_j1.get_rect()
                r_j1.centerx=p2x
                p2x=p2x+40
                r_j1.centery=50
                screen.blit(img_j1,r_j1)


        pygame.display.flip()

main()