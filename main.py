import pygame as pg
from models.constantes import *
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

#acomodamos ancho y alto y tmb cargamos la imagen de fondo
background_img = pg.image.load(r'pygame_2/assets/img/background/goku_house.png')
background_img = pg.transform.scale(background_img,(ANCHO_VENTANA,ALTO_VENTANA))

vegeta = Jugador (0,0,frame_rate= 70 ,speed_walk=10,speed_run=40)

while juego_ejecutandose:

    lista_eventos = pg.event.get()

    for evento in lista_eventos:
        match evento.type:
            # case pg.KEYDOWN:
            #     if evento.key == pg.K_SPACE:
            #         vegeta.jump(True)
            # case pg.KEYUP:
            #     if evento.key == pg.K_SPACE: 
            #         vegeta.jump(False)
            case pg.QUIT:
                print("Estoy CERRANDO el juego")
                juego_ejecutandose = False
                break

    lista_teclas_presionadas = pg.key.get_pressed()
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.walk('Right') 
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.walk('Left') 
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.stay()

    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        vegeta.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        vegeta.run('Left') 

    if lista_teclas_presionadas[pg.K_SPACE] :
        vegeta.jump(True) 

    screen.blit(background_img,background_img.get_rect()) 
    delta_ms = clock.tick(FPS)  #da una frecuencia da valores y en este caso cuando se 16 el valor y apriete la tecla e ,va amostrar el mensaje
    vegeta.update(delta_ms)
    vegeta.draw(screen)
    pg.display.update() #puedo usar flip() , pero el update() se adapta mejor y no pierde calidad

pg.quit()


