import function as f

f.inicializar()

f.insertar_personaje("\cristal")
done = False
while not done:
    for event in f.pg.event.get():
        if event.type == f.pg.QUIT:
            done = True
#### Update the the display and wait ####

f.pg.quit()