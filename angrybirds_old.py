import pygame,random,math,os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25)

pygame.init()
pygame.mixer.init()

app_exit=False

black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
green=(0,255,100)
blue=(0,0,255)
cyan=(0,255,255)

display=pygame.display.set_mode((1600,900))
pygame.display.set_caption("ANGRY BIRDS")
display.fill(white)

clock=pygame.time.Clock()

bird_vel=0

slingcentre=[325,500]
sling=pygame.image.load("sling.PNG")
sling=pygame.transform.scale(sling,(50,50))

red=pygame.image.load("red2.GIF")
red=pygame.transform.scale(red,(30,30))
redcentre=[15,15]
redpos=[310,485]
redvelx,redvely=0,0

slingengaged=0

grav=2



def slingrend(x,y):
    display.blit(sling,(x,y))

def redclear(pos):
    pygame.draw.rect(display,white,(pos[0],pos[1],30,30))

def redrend(x,y):
    display.blit(red,(x,y))

def strapclear(pos):
    pygame.draw.line(display,white,(300,500),(pos[0]+redcentre[0],pos[1]+redcentre[1]),3)
    pygame.draw.line(display,white,(350,500),(pos[0]+redcentre[0],pos[1]+redcentre[1]),3)    

def strap(birdx,birdy):
    pygame.draw.line(display,black,(300,500),(birdx+redcentre[0],birdy+redcentre[1]),3)
    pygame.draw.line(display,black,(350,500),(birdx+redcentre[0],birdy+redcentre[1]),3)

def launchvel(pos):
    velx=(slingcentre[0]-pos[0]-redcentre[0])/6
    vely=(slingcentre[1]-pos[1]-redcentre[1])/6
    return velx,vely

while not app_exit:#loop to control entry and exit from application

    game_exit=False

    while  not game_exit:
        
        for event in pygame.event.get():
        
            if event.type==pygame.QUIT:
                game_exit=True
                app_exit=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(redpos[0],redpos[0]+30):
                    if pygame.mouse.get_pos()[1] in range(redpos[1],redpos[1]+30):
                        slingengaged=1
            if event.type==pygame.MOUSEBUTTONUP:
                if slingengaged==1:
                    redvelx,redvely=launchvel(redpos)
                strapclear(redpos)
                slingengaged=0

        if slingengaged==1:
            redclear(redpos)
            strapclear(redpos)
            if ((slingcentre[0]-pygame.mouse.get_pos()[0])**2+(slingcentre[1]-pygame.mouse.get_pos()[1])**2)**0.5<=60:
                redpos=[pygame.mouse.get_pos()[0]-redcentre[0]+redvelx,pygame.mouse.get_pos()[1]-redcentre[1]+redvely]
            strap(redpos[0],redpos[1])

        redclear(redpos)                               
        slingrend(300,500)

        if slingengaged==0:
            redpos=[redpos[0]+redvelx,redpos[1]+redvely]
            strap(310,485)

        redrend(redpos[0],redpos[1])
        
        pygame.display.update()

        clock.tick(60)

pygame.quit()
quit()
