import pygame #traer pygame

pygame.init()
'Espacio de constantes y colores'
COLORES={
        'AZUL':(0,0,254),
        'ROJO':(254,0,0),
        'VERDE':(0,254,0),
        'BLANCO':(254,254,254),
        'NEGRO':(0,0,0),
        'AMARILLO':(254,254,0)
}

DIMENSION=[400,400] #constante de dimension

pantalla=pygame.display.set_mode(DIMENSION) #crea la pantalla con las dimensiones establecidas
pygame.display.set_caption('Primer juego') #titulo a la pantalla

hecho=True

while hecho:
    
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            hecho=False
        
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_RIGHT:
                pantalla.fill(COLORES['VERDE'])
            elif evento.key==pygame.K_LEFT:
                pantalla.fill(COLORES['AZUL'])
                pygame.draw.line(pantalla,COLORES['AMARILLO'],[0,200],[400,200],20)
                pygame.draw.rect(pantalla,COLORES['AMARILLO'],[50,0,200,200])
        else:
            pantalla.fill(COLORES['ROJO'])
            pygame.draw.rect(pantalla,COLORES['BLANCO'],[50,100,100,100])
            pygame.draw.line(pantalla,COLORES['AMARILLO'],[50,102],[100,200],5)
    
    
    #pantalla.fill(COLORES['ROJO']) #rellena la pantalla de un color
    
    pygame.display.flip() # actualiza los elementos
    
    