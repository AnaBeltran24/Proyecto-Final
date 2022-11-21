import pygame
pygame.init()

pantalla=pygame.display.set_mode((750,500))
white=(255,255,255)
black=(0,0,0)
pygame.display.set_caption("Juego Pong")
class Jugadores(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0
class pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([12, 12])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = 1
        self.dy = 1
Jugador1=Jugadores()
Jugador1.rect.x=25
Jugador1.rect.y=225

Jugador2=Jugadores()
Jugador2.rect.x=715
Jugador2.rect.y=225

Jugadores_speed = 80

pelotaAJ=pelota()
pelotaAJ.rect.x=375
pelotaAJ.rect.y=225

all_sprites=pygame.sprite.Group()
all_sprites.add(Jugador1, Jugador2, pelotaAJ)


def dpantalla():
    pantalla.fill(black)
    font = pygame.font.SysFont('Comic Sans',30)
    text= font.render('PONG',False,white)
    textRect=text.get_rect()
    textRect.center=(750//2, 25)
    pantalla.blit(text,textRect)
    textJ1= font.render('Jugador 1',False,white)
    textRectJ1=text.get_rect()
    textRectJ1.center=(170//2, 14)
    pantalla.blit(textJ1,textRectJ1)
    textJ2= font.render('Jugador 2',False,white)
    textRectJ2=text.get_rect()
    textRectJ2.center=(1150//2, 14)
    pantalla.blit(textJ2,textRectJ2)
    J1_puntaje=font.render(str(Jugador1.points),False,white)
    J1Rect=J1_puntaje.get_rect()
    J1Rect.center=(100,50)
    pantalla.blit(J1_puntaje,J1Rect)
    J2_puntaje=font.render(str(Jugador2.points),False,white)
    J2Rect=J2_puntaje.get_rect()
    J2Rect.center=(600,50)
    pantalla.blit(J2_puntaje,J2Rect)
    pygame.draw.line (pantalla,white,(376,740), (376,39),3)
    all_sprites.draw(pantalla)
    pygame.display.update()


Juego=True
while Juego:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Juego=False
    key =pygame.key.get_pressed()
    if key [pygame.K_w]:
        Jugador1.rect.y += -Jugadores_speed
    if key [pygame.K_s]:
        Jugador1.rect.y += Jugadores_speed
    if key [pygame.K_UP]:
        Jugador2.rect.y += -Jugadores_speed
    if key [pygame.K_DOWN]:
        Jugador2.rect.y += Jugadores_speed
    
    pelotaAJ.rect.x += pelotaAJ.speed * pelotaAJ.dx
    pelotaAJ.rect.y += pelotaAJ.speed * pelotaAJ.dy
    
    if pelotaAJ.rect.y > 490:
        pelotaAJ.dy = -1
    if pelotaAJ.rect.x > 740:
        pelotaAJ.rect.x, pelotaAJ.rect.y = 375, 250
        pelotaAJ.dx = -1
        Jugador1.points += 1
    if pelotaAJ.rect.y < 10:
        pelotaAJ.dy = 1
    if pelotaAJ.rect.x < 10:
        pelotaAJ.rect.x, pelotaAJ.rect.y = 375, 250
        pelotaAJ.dx = 1
        Jugador2.points +=1
    if Jugador1.rect.colliderect(pelotaAJ.rect):
        pelotaAJ.dx=1
    if Jugador2.rect.colliderect(pelotaAJ.rect):
        pelotaAJ.dx=-1
    
    dpantalla()

pygame.quit
