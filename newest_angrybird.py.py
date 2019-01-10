import pygame,math,slicer,thread
#Modify high score file
pygame.init()

app_exit=False
game_exit=False

black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
green=(0,255,100)
blue=(0,0,255)
cyan=(0,255,255)

#display=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
display=pygame.display.set_mode((1400,1080))
pygame.display.set_caption("ANGRY BIRDS")
display.fill(white)
pygame.display.update()

img=slicer.blocks().wooden_block()

tiny=pygame.image.load("tiny.png")
tiny=pygame.transform.scale(tiny,(80,8))
col=pygame.image.load("col.png")
col=pygame.transform.rotate(col,90)
col=pygame.transform.scale(col,(12,120))

minion=pygame.image.load("pigprime.gif")
minion=pygame.transform.scale(minion,(40,40))
pigvel=[]
piglist=[]
exterminator=[]

clock=pygame.time.Clock()

slingcentre=[]   
sling=pygame.image.load("sling.PNG")
sling=pygame.transform.scale(sling,(50,50))
slingpos=[]

red=pygame.image.load("red2.GIF")
red=pygame.transform.scale(red,(30,30))
redcentre=[15,15]
redpos=[]
redvelx,redvely=0,0
redsub=3
subpos=[]
play=1
bird_vel=0

slingengaged=2
slingpast=2
score=0

grav=.065
gravengaged=0

e=0.5

f=.95
fricgage=0

hard_r=[]
hard_w=[]
w_guide=[]
trash=[]
colvel=[]

skip=0

collidevar=0

poofp=[pygame.image.load("poof1.png"),pygame.image.load("poof2.png"),pygame.image.load("poof3.png"),pygame.image.load("poof4.png")]
poofp=[pygame.transform.scale(poofp[0],(40,40)),pygame.transform.scale(poofp[1],(40,40)),pygame.transform.scale(poofp[2],(40,40)),pygame.transform.scale(poofp[3],(40,40))]

poofb=[pygame.image.load("poof1.png"),pygame.image.load("poof2.png"),pygame.image.load("poof3.png"),pygame.image.load("poof4.png")]
poofb=[pygame.transform.scale(poofp[0],(30,30)),pygame.transform.scale(poofp[1],(30,30)),pygame.transform.scale(poofp[2],(30,30)),pygame.transform.scale(poofp[3],(30,30))]

endgame=pygame.image.load("background.png")
endgame=pygame.transform.scale(endgame,(1366,768))

win,loss=0,0

fonts=pygame.font.SysFont("Comic Sans",80)
fonts1=pygame.font.SysFont("Comic Sans",33)

setup=1

def menu():
    global grey
    
    cond=True
        
    while cond:

        imag=pygame.image.load("Menubackground.PNG")
        imag=pygame.transform.scale(imag,(1366,768))
        display.fill(white)
        display.blit(imag,(0,0))

        end=pygame.image.load("quit.PNG")
        end=end.subsurface(140,160,320,130)
        end=pygame.transform.scale(end,(200,60))
        display.blit(end,(1146,20))

        fonts=pygame.font.SysFont("Comic Sans",50)
        
        label=fonts.render("MENU",True,cyan)
        label2=fonts.render("SELECT LEVEL",True,cyan)
        label3=fonts.render("REPLAYS",True,cyan)
        label4=fonts.render("INSTRUCTIONS",True,cyan)
        
        pygame.draw.rect(display,(255,0,0),(480,90,400,80))
        pygame.draw.rect(display,(255,0,0),(480,260,400,80))
        pygame.draw.rect(display,(255,0,0),(480,430,400,80))
        pygame.draw.rect(display,(255,0,0),(480,600,400,80))

        display.blit(label,[680-label.get_width()/ 2,110])
        display.blit(label2,[680-label2.get_width()/ 2,280])
        display.blit(label3,[680-label3.get_width()/ 2,450])
        display.blit(label4,[680-label4.get_width()/ 2,620])
        
        pygame.display.update()

        button=0

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                button=1

            if event.type==pygame.MOUSEBUTTONUP:
                pos=event.pos

                if button==1:

                    if pos[0] in range(465,896) and pos[1] in range(240,351):
                        ch=levelselect()
                        if ch!=0:
                            return ch

                    elif pos[0] in range(465,896) and pos[1] in range(410,531):
                        pass

                    elif pos[0] in range(465,896) and pos[1] in range(580,701):
                        instructions()

                    elif pos[0] in range(1126,1376) and pos[1] in range(0,101):
                        return 0
                button=0
        button=0

        clock.tick(20)

def  levelselect():

     display.fill(white)

     imag=pygame.image.load("Menubackground.PNG")
     imag=pygame.transform.scale(imag,(1366,768))
     display.fill(white)
     display.blit(imag,(0,0))

     back=pygame.image.load("back.PNG")
     back=pygame.transform.scale(back,(100,50))
     display.blit(back,(0,0))

     no_of_levels=2

     x,y=60,200

     for i in range((no_of_levels/5)+1):
         for j in range(5):
             if i*5+j==no_of_levels:
                 break
             pygame.draw.rect(display,(255,0,0),(x,y,200,40))
             level_n=str(i*5+j+1)
             label=fonts1.render("LEVEL: "+level_n,True,cyan)
             display.blit(label,[x+100-label.get_width()/ 2,y+10])
             x+=261
         x=60
         y+=145

     pygame.display.update()

     buttondown=False

     while True:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                buttondown=True
                
            if event.type==pygame.MOUSEBUTTONUP:

                if  buttondown==True:
                    
                    buttondown=False
                    
                    pos=event.pos

                    if pos[0] in range(105) and pos[1] in range(55):
                        return 0
                    
                    x,y=60,200
                    
                    for i in range((no_of_levels/5)+1):
                        for j in range(5):
                            if i*5+j==no_of_levels:
                                break
                            if  pos[0] in range(x-5,x+205) and pos[1] in range(y-5,y+45):
                                level_n=i*5+j+1
                                return level_n
                            x+=261
                        x=60
                        y+=145
    
def instructions():
    global cyan
    imag=pygame.image.load("Menubackground.PNG")
    imag=pygame.transform.scale(imag,(1366,768))
    display.fill(white)
    display.blit(imag,(0,0))

    font=pygame.font.SysFont("Copperplate Gothic Bold",50)
    font2=pygame.font.SysFont("Copperplate Gothic Bold",80)
    text("Welcome to Angry Birds",50,font2)
    text("Use the birds to kill all the pigs",120,font)
    text("Launch the bird:",170,font)
    text("Click and hold the bird loaded in the sling ",220,font)
    text("Use the MOUSE to aim",270,font)
    text("Release the mousebutton to launch the bird",320,font)
    text("Happy Slinging!!!",370,font)

    back=pygame.image.load("back.PNG")
    back=pygame.transform.scale(back,(100,50))
    display.blit(back,(0,0))

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(105) and pos[1] in range(55):
                    return

def text(msg,pos,fonts):
    
    lbl=fonts.render(msg,True,(255,0,0))
    display.blit(lbl,[683-lbl.get_width()/ 2,pos])

def lvl1():
    global hard_r,hard_w,w_guide,colvel,pigvel,piglist,slingpos,slingcentre,subpos,redpos
    r1=pygame.draw.rect(display,black,(700,600,700,200))
    r2=pygame.draw.rect(display,black,(1200,350,200,250))
    r3=pygame.draw.rect(display,black,(180,700,110,50))
    r4=pygame.draw.rect(display,black,(0,750,290,50))
    r5=pygame.draw.rect(display,black,(180,700,520,70))
    
    i1=display.blit(col,(750,480))
    i2=display.blit(col,(900,480))
    col2=pygame.transform.scale(col,(12,170))
    i3=display.blit(col2,(1050,430))

    i4=display.blit(tiny,(716,472))
    i5=display.blit(tiny,(866,472))
    i6=display.blit(tiny,(1016,422))

    colvel=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    m1=display.blit(minion,(736,432))
    m2=display.blit(minion,(886,432))
    m3=display.blit(minion,(1036,382))
    m4=display.blit(minion,(1220,310))

    pigvel=[[0,0],[0,0],[0,0],[0,0]]

    hard_r=[r1,r2,r3,r4,r5]
    hard_w=[[i1,i2],[i3],[i4,i5,i6]]
    w_guide=[col,col2,tiny]
    piglist=[m1,m2,m3,m4]
    slingpos=[200,650]
    slingcentre=[225,650]
    subpos=[140,720]
    redpos=[210,635]

def lvl2():
    global hard_r,hard_w,w_guide,colvel,pigvel,piglist,slingpos,slingcentre,subpos,redpos
    r1=pygame.draw.rect(display,black,(0,370,500,400))
    r2=pygame.draw.rect(display,black,(600,640,800,130))
    r3=pygame.draw.rect(display,black,(1340,0,30,645))
    r4=pygame.draw.rect(display,black,(800,200,350,70))
    
    i1=display.blit(col,(900,520))
    i2=display.blit(col,(900,400))

    colvel=[[0,0],[0,0]]

    m1=display.blit(minion,(600,604))
    m2=display.blit(minion,(1040,604))
    m3=display.blit(minion,(955,164))

    pigvel=[[0,0],[0,0],[0,0]]

    hard_r=[r1,r2,r3,r4]
    hard_w=[[i1,i2]]
    w_guide=[col]
    piglist=[m1,m2,m3]
    slingpos=[300,320]
    slingcentre=[325,320]
    subpos=[200,340]
    redpos=[310,305]

def lvl3():
    global hard_r,hard_w,w_guide,colvel,pigvel,piglist,slingpos,slingcentre,subpos,redpos
    pass

def poofanim(x,y,c):
    global poofb,poofp
    if c=='p':
        pygame.mixer.music.load("poof.mp3")
        pygame.mixer.music.play()
        for j in poofp:
            display.blit(j,[x,y])
            pygame.time.wait(130)
            pygame.draw.rect(display,white,(x,y,40,40))
            pygame.display.update()
    elif c=='b':
        pygame.mixer.music.load("birddead.mp3")
        pygame.mixer.music.play()
        for j in poofb:
            display.blit(j,[x,y])
            pygame.time.wait(130)
            pygame.draw.rect(display,white,(x,y,30,30))
            pygame.display.update()
        
def victory():
    global endgame,green,app_exit,fonts,grey,fonts1,setup
    f=open("Highscore","a+")
    f.seek(0)
    if score>int(f.read()):
        f.close()
        f=open("Highscore","w+")
        f.write(str(score))
        f.close()
    f=open("Highscore","a+")
    f.seek(0)
    label=fonts.render("LEVEL CLEARED",True,grey)
    label1=fonts1.render("SCORE: "+str(score),True,grey)
    label2=fonts1.render("HIGHSCORE: "+f.read(),True,grey)
    label3=fonts1.render("REPLAY",True,grey)
    label4=fonts1.render("MENU",True,grey)
    label5=fonts1.render("QUIT",True,grey)
    while True:
        for event in pygame.event.get():#loop to handle events
           if event.type==pygame.MOUSEBUTTONDOWN:
               p=pygame.mouse.get_pos()
               if p[0]>40 and p[0]<280 and p[1]>540 and p[1]<660:
                   display.fill(white)
                   pygame.display.update()
                   return
               elif  p[0]>560 and p[0]<800 and p[1]>540 and p[1]<660:
                   setup=1
                   return
               elif p[0]>1080 and p[0]<1320 and p[1]>540 and p[1]<660:
                   app_exit=True
                   return
                                
        display.blit(endgame,(0,0))
        pygame.draw.rect(display,green,(400,300,550,100))
        pygame.draw.rect(display,green,(60,550,200,60))
        pygame.draw.rect(display,green,(320,550,200,60))
        pygame.draw.rect(display,green,(580,550,200,60))
        pygame.draw.rect(display,green,(840,550,200,60))
        pygame.draw.rect(display,green,(1100,550,200,60))
        display.blit(label,[675-label.get_width()/ 2,325])
        display.blit(label3,[160-label3.get_width()/2,565])
        display.blit(label1,[420-label1.get_width()/2,565])
        display.blit(label4,[680-label4.get_width()/ 2,565])
        display.blit(label2,[940-label2.get_width()/ 2,565])
        display.blit(label5,[1200-label5.get_width()/ 2,565])
        pygame.display.update()
        pygame.time.wait(25)

def lose():
    global endgame,green,app_exit,fonts,grey,setup
    label=fonts.render("LEVEL FAILED",True,grey)
    label2=fonts.render("REPLAY",True,grey)
    label3=fonts.render("MENU",True,grey)
    label4=fonts.render("QUIT",True,grey)
    while True:
        for event in pygame.event.get():#loop to handle events
           if event.type==pygame.MOUSEBUTTONDOWN:
               p=pygame.mouse.get_pos()
               if p[0]>115 and p[0]<435 and p[1]>540 and p[1]<660:
                   display.fill(white)
                   pygame.display.update()
                   return
               elif  p[0]>540 and p[0]<860 and p[1]>540 and p[1]<660:
                   setup=1
                   return
               elif p[0]>965 and p[0]<1285 and p[1]>540 and p[1]<660:
                   app_exit=True
                   return
                                
        display.blit(endgame,(0,0))
        pygame.draw.rect(display,green,(400,300,550,100))
        pygame.draw.rect(display,green,(125,550,300,100))
        pygame.draw.rect(display,green,(550,550,300,100))
        pygame.draw.rect(display,green,(975,550,300,100))
        display.blit(label,[675-label.get_width()/ 2,325])
        display.blit(label2,[275-label2.get_width()/ 2,575])
        display.blit(label3,[700-label3.get_width()/ 2,575])
        display.blit(label4,[1125-label4.get_width()/ 2,575])
        pygame.display.update()
        pygame.time.wait(25)
        
def slingrend(x,y):
    display.blit(sling,(x,y))

def redclear(pos):
    pygame.draw.rect(display,white,(pos[0],pos[1],30,30))

def redrend(x,y):
    display.blit(red,(x,y))

def strapclear(pos):
    global slingpos
    pygame.draw.line(display,white,(slingpos[0],slingpos[1]),(pos[0]+redcentre[0],pos[1]+redcentre[1]),3)
    pygame.draw.line(display,white,(slingpos[0]+50,slingpos[1]),(pos[0]+redcentre[0],pos[1]+redcentre[1]),3)    

def strap(birdx,birdy):
    global slingpos
    pygame.draw.line(display,black,(slingpos[0],slingpos[1]),(birdx+redcentre[0],birdy+redcentre[1]),3)                     
    pygame.draw.line(display,black,(slingpos[0]+50,slingpos[1]),(birdx+redcentre[0],birdy+redcentre[1]),3)

def launchvel(pos):
    velx=(slingcentre[0]-pos[0]-redcentre[0])/7
    vely=(slingcentre[1]-pos[1]-redcentre[1])/7
    return velx,vely

def oob():
    global redvelx,redvely,redpos
    if redpos[0]>1370 or redpos[0]<-30 or redpos[1]>770 :
        redvelx,redvely=0,0

def substitutes():
    global redsub,red,subpos
    x,y=subpos[0],subpos[1]
    if redsub>-1:
        for i in range(3):
            pygame.draw.rect(display,white,(x,y,30,30))
            if i<redsub:
                display.blit(red,(x,y))
            x-=40

def reddead():
    global redsub,slingengaged,deadcount,redvelx,redvely,redpos,gravengaged,collidevar,isreddead
    if slingengaged==0 and math.fabs(redvelx)<0.05 and math.fabs(redvely)<=0.065:
        thread.start_new_thread(poofanim,(redpos[0],redpos[1],'b'))
        redsub-=1
        isreddead=True
        if redsub!=-1:
            slingengaged=2
            gravengaged=0
            redvelx,redvely=0,0
            collidevar=0
            redclear(redpos)
            redreset()

def redreset():
    global redpos,slingpos
    redpos=[slingpos[0]+10,slingpos[1]-15]
        
def draw():
    global hard_r,hard_p,hard_w,w_guide,trash,piglist,exterminator,poofp,score
    for i in hard_r:
        pygame.draw.rect(display,black,i)
    for i in range(len(hard_w)):
        for j in hard_w[i]:
            display.blit(w_guide[i],j)
    for i in trash:
        i=list(i)
        pygame.draw.rect(display,white,i)
    for i in piglist:
        display.blit(minion,i)
    for i in exterminator:
        thread.start_new_thread(poofanim,(piglist[i][0],piglist[i][1],"p"))
        score+=50        
    trash=[]

def grav_w_detect():
    global hard_w,white,grav,w_guide
    for i in range(len(hard_w)):
        for k in range(len(hard_w[i])):
            for j in range(hard_w[i][k][0],hard_w[i][k][0]+hard_w[i][k][2]+1,5):
                if display.get_at((j,hard_w[i][k][1]+hard_w[i][k][3]+2))!=(255,255,255,255):
                    break
            else:
                pygame.draw.rect(display,white,hard_w[i][k])
                hard_w[i][k][1]*=1.005
                display.blit(w_guide[i],hard_w[i][k])

def grav_p_detect():
    global piglist,minion
    for i in range(len(piglist)):
        for j in range(piglist[i][0],piglist[i][0]+41):
            if display.get_at((j,piglist[i][1]+42))!=(255,255,255,255):
                break
        else:
            pygame.draw.rect(display,white,piglist[i])
            piglist[i][1]*=1.005
            display.blit(minion,piglist[i])
        

def pigcol():
    global redpos,piglist,exterminator,redvelx,redvely
    ct=0
    for i in piglist:
        if redpos[0]<=i[0]+i[2] and redpos[0]>=i[0] or redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+i[2]:# end & start
            #top
                if redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+30:
                    if ct not in exterminator:
                        exterminator.append(ct)
                        
            #bottom
                elif redpos[1]<=i[1]+i[3] and redpos[1]>=i[1]+i[3]-20:
                    if ct not in exterminator:
                        exterminator.append(ct)
                        
        if  redpos[1]<=i[1]+i[3] and redpos[1]>=i[1] or redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+i[3]:# start & end
            #left
        
                if redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+20:
                    if ct not in exterminator:
                        exterminator.append(ct)

            #right
                elif redpos[0]<=i[0]+i[2] and redpos[0]>=i[0]+i[2]-20:
                    if ct not in exterminator:
                        exterminator.append(ct)
        ct+=1

def terminate():
    global exterminator,piglist
    for i in exterminator:
        del piglist[i]
    exterminator=[]
    

def destroyer(destroy):
    global hard_w,trash,score
    for i in destroy:
        trash.append(hard_w[i[0]][i[1]])
        del hard_w[i[0]][i[1]]
        score+=25

def newcol_w():
    global hard_w,redpos,redvelx,redvely
    destroy=[]
    ct1=0
    for j in hard_w:
        ct2=0
        for i in j:
            appendct=0
            if redpos[0]<=i[0]+i[2] and redpos[0]>=i[0] or redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+i[2]:# end & start
            #top
                if redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+30:
                    if redvely>1.7:
                        if appendct==0:
                            destroy.append([ct1,ct2])
                            appendct+=1
                        redvely/=1.9
                    else:
                        redvely=e*(-redvely)
                        redvelx=f*redvelx
                        
            #bottom
                elif redpos[1]<=i[1]+i[3] and redpos[1]>=i[1]+i[3]-20:
                    if redvely<-1.7:
                        if appendct==0:
                            destroy.append([ct1,ct2])
                            appendct+=1
                        redvely/=1.9
                    else:
                        redvely=e*(-redvely)
                        redvelx=f*redvelx
                        
            if  redpos[1]<=i[1]+i[3] and redpos[1]>=i[1] or redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+i[3]:# start & end
            #left
        
                if redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+20:
                    if redvelx>1.7:
                        if appendct==0:
                            destroy.append([ct1,ct2])
                            appendct+=1
                        redvelx/=1.9
                    else:
                        redvely=f*(redvely)
                        redvelx=e*(-redvelx)

            #right
                elif redpos[0]<=i[0]+i[2] and redpos[0]>=i[0]+i[2]-20:
                    if redvelx<-1.7:
                        if appendct==0:
                            destroy.append([ct1,ct2])
                            appendct+=1
                        redvelx/=1.9
                    else:
                        redvely=f*(redvely)
                        redvelx=e*(-redvelx)
            ct2+=1

        ct1+=1
        
    if destroy!=[]:
        destroyer(destroy)
    

def newcol_r():
    global hard_r,redpos,redvelx,redvely,e,f
    for i in hard_r:
        if redpos[0]<=i[0]+i[2] and redpos[0]>=i[0] or redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+i[2]:# end & start
        #top
            if redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+30:
                if redvely>0:
                    if redvely>0.7:
                        pygame.mixer.music.load("ouch.mp3")
                        pygame.mixer.music.play()
                    redvely=e*(-redvely)
                    redvelx=f*redvelx
                if math.fabs(redvely)<0.1:
                    redvely=0
        #bottom
            elif redpos[1]<=i[1]+i[3] and redpos[1]>=i[1]+i[3]-20:                
                if redvely<0:
                    pygame.mixer.music.load("ouch.mp3")
                    pygame.mixer.music.play()
                    redvely=e*(-redvely)
                    redvelx=f*redvelx

        if  redpos[1]<=i[1]+i[3] and redpos[1]>=i[1] or redpos[1]+30>=i[1] and redpos[1]+30<=i[1]+i[3]:# start & end
        #left
    
            if redpos[0]+30>=i[0] and redpos[0]+30<=i[0]+20:
                if redvelx>0:
                    pygame.mixer.music.load("ouch.mp3")
                    pygame.mixer.music.play()
                    redvely=f*(redvely)
                    redvelx=e*(-redvelx)
                
        #right
            elif redpos[0]<=i[0]+i[2] and redpos[0]>=i[0]+i[2]-20:
                if redvelx<0:
                    pygame.mixer.music.load("ouch.mp3")
                    pygame.mixer.music.play()
                    redvely=f*(redvely)
                    redvelx=e*(-redvelx)


while app_exit==False:

    slingengaged=2
    slingpast=2
    grav=.065
    gravengaged=0   
    fricgage=0

    hard_r=[]
    hard_w=[]
    w_guide=[]
    trash=[]
    colvel=[]

    skip=0
    collidevar=0

    redcentre=[15,15]
    #redpos=[210,635]
    redvelx,redvely=0,0
    if play!=1:
        redsub=4
    bird_vel=0

    pigvel=[]
    piglist=[]
    exterminator=[]

    score=0

    if setup==1:
        cmd=menu()
    display.fill(white)
    pygame.display.update()
    if cmd==0:
        break
    fn_name='lvl'+str(cmd)
    globals()[fn_name]()#calling fn from name stored in a string    
    setup=0

    pygame.event.clear()    

    while game_exit==False:
        
        for event in pygame.event.get():#loop to handle events
           if event.type==pygame.QUIT:
                game_exit=True
                app_exit=True

           if event.type==pygame.KEYDOWN:
               game_exit=True
               app_exit=True

           if event.type==pygame.MOUSEBUTTONDOWN and slingengaged!=0:
               if pygame.mouse.get_pos()[0] in range(int(redpos[0]),int(redpos[0]+30)):
                   if pygame.mouse.get_pos()[1] in range(int(redpos[1]),int(redpos[1]+30)):
                       slingengaged=1
                       
           if event.type==pygame.MOUSEBUTTONUP:
               if slingengaged==1:
                   redvelx,redvely=launchvel(redpos)
                   gravengaged=1
               strapclear(redpos)
               slingengaged=0
               
        if slingengaged==1:
             redclear(redpos)
             strapclear(redpos)
             if ((slingcentre[0]-pygame.mouse.get_pos()[0])**2+(slingcentre[1]-pygame.mouse.get_pos()[1])**2)**0.5<=70:
                 redpos=[pygame.mouse.get_pos()[0]-redcentre[0]+redvelx,pygame.mouse.get_pos()[1]-redcentre[1]+redvely]
             strap(redpos[0],redpos[1])
        redclear(redpos)                               
        slingrend(slingpos[0],slingpos[1])
        draw()
        terminate()
        if collidevar>=3 and skip==0:
            newcol_r()
            pigcol()
            newcol_w()
            grav_w_detect()
            grav_p_detect()

        if slingengaged==0:
            collidevar+=1
            
        if slingengaged==0 or slingengaged==2:
            if gravengaged==1 and fricgage==0:
                redpos=[redpos[0]+redvelx,redpos[1]+redvely]
                redvely+=grav
            else:
                redpos=[redpos[0]+redvelx,redpos[1]+redvely]
            strap(slingpos[0]+10,slingpos[1]-10)
            
        redrend(redpos[0],redpos[1])
        
        try:
            if skip==int((redvelx/redvely)*redvely/2)+1:
                skip=0
        except ZeroDivisionError:
            pass
        
        if skip!=0:
            skip+=1

        slingpast=slingengaged
        
        oob()
        substitutes()
        reddead()

        if len(piglist)==0 or redsub==-1:
            if len(piglist)==0:
                win=1
                if isreddead==True:
                    break
            else:
                loss=1
                if isreddead==True:
                    break
        
        pygame.display.update()

        clock.tick(60)

        isreddead=False

    pygame.time.wait(1000)

    if win==1:
        pygame.mixer.music.load("lvlwin.mp3")
        pygame.mixer.music.play()
        win=0
        score=score+(redsub+1)*200
        victory()

    elif loss==1:
        pygame.mixer.music.load("lvllose.mp3")
        pygame.mixer.music.play(2)
        loss=0
        lose()
    play+=1
    
pygame.quit()
quit()
#blit(source, dest, area=None, special_flags = 0)
#img.subsurface(row,col,width,ht)

##def newcol_p():
##    global hard_p,redpos,redvelx,redvely,e,f,skip,fricgage
##    fricgage=0
##    try:
##        for i in hard_p:
##            centx,centy=0,0
##            for j in i:
##                centx+=j[0]
##                centy+=j[1]
##            centx/=len(i)
##            centy/=len(i)
##            for j in range(len(i)-1):
##                k=j+1
##                if i[k][0]>i[j][0]:
##                    highx,lowx=i[k][0],i[j][0]
##                else:
##                    highx,lowx=i[j][0],i[k][0]
##                if i[k][1]>i[j][1]:
##                    highy,lowy=i[k][1],i[j][1]
##                else:
##                    highy,lowy=i[j][1],i[k][1]
##                m=(float(i[k][1])-i[j][1])/(i[k][0]-i[j][0])
##                theta=math.atan(m)
##                s1=m*(redpos[0]-i[j][0])+i[j][1]-redpos[1]
##                s2=m*(redpos[0]+30-i[j][0])+i[j][1]-redpos[1]
##                s3=m*(redpos[0]-i[j][0])+i[j][1]-redpos[1]-30
##                s4=m*(redpos[0]+30-i[j][0])+i[j][1]-redpos[1]-30
##                t=m*(centx-i[j][0])+i[j][1]-centy
##                p1,p2,p3,p4=s1*t,s2*t,s3*t,s4*t
##                if p1>0 or p2>0 or p3>0 or p4>0:
##                    if redpos[0]<highx and redpos[0]>lowx or redpos[0]+30<highx and redpos[0]+30>lowx:
##                        if redpos[1]<highy and redpos[1]>lowy or redpos[1]+30<highy and redpos[1]+30>lowy:
##                            print "Yee"
##                            vn=-e*(redvelx*math.sin(theta)+redvely*math.cos(theta))
##                            vt=f*(redvelx*math.cos(theta)+redvely*math.sin(theta))
##                            redvelx=vt*math.cos(theta)+vn*math.sin(theta)
##                            redvely=vt*math.sin(theta)+vn*math.cos(theta)
##                            skip=1
##                            fricgage=1
##                            
##    except ZeroDivisionError:
##        pass







