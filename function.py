import pygame as pg

personajes = []
screen = []
def inicializar():
    pg.display.init()
    
    global screen
    
    screen = pg.display.set_mode((500,500))

    #escenario = pg.Surface((500,500))
    escenario = pg.image.load(".\imagenes\escenario\escenario.jpg")

    screen.blit(escenario,[0,0])


    plataforma = pg.image.load(".\imagenes\escenario\plataforma.png")
    plataforma = pg.transform.scale(plataforma,[300,200])

    screen.blit(plataforma,[100,200])

    pg.display.flip()

def insertar_personaje(nombre):
    personaje = pg.image.load(".\imagenes" + nombre + "\stand.png")
    personaje = pg.transform.scale(personaje,[100,100])
    screen.blit(personaje,[100,180])
    pg.display.flip()
