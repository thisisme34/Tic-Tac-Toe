# import and initailize the pygame library
import pygame
import sys
# for sys.exit()
winner=None
game_over=False
def run_game():
    global winner
    global game_over
    def draw_grid(screen):
        start=70
        end=430
        width=(end-start)/3
        add=width
        for i in range(0,2):
            # draw vertical lines
            pygame.draw.line(screen,(255,0,255),(start+add,start),(start+add,end),width=5)
            #draw horizontal lines
            pygame.draw.line(screen,(255,0,255),(start,start+add),(end,start+add),width=5)
            add=add+width
    table=[]


    #actual_table
    for i in range(3):
        row=[0]*3
        table.append(row)
    image1=pygame.image.load("tic tac toe/O.jpeg")
    image2=pygame.image.load("tic tac toe/X.jpeg")
    image1=pygame.transform.scale(image1,(110,110))
    image2=pygame.transform.scale(image2,(110,110))

    def pic_board(screen):
            row=0
            for x in table:
                column=0
                for y in x:
                    if y==1:
                        screen.blit(image1,(70+column*120+3,70+row*120+3))
                    elif y==-1:
                        screen.blit(image2,(70+column*120+3,70+row*120+3))
                    column+=1
                row+=1

    again_rect=pygame.Rect(120,430,255,70)
    def draw_winner(winner,screen):
        font=pygame.font.SysFont("gabriola",70)
        
        if winner==None:
            win_text="It's a tie!!!"
        else:
            win_text="Player  "+str(winner)+" wins"
            
        win_img=font.render(win_text,True,(0,0,0))
        screen.blit(win_img,(135,10))
        #again text
        again_text="Play  Again"
        again_img=font.render(again_text,True,(0,0,139))
        screen.blit(again_img,(130,430))
        pygame.draw.rect(screen,(50,50,50),again_rect,width=5,border_radius=40)


    def check(turn):
        global winner
        global game_over
        x=0
        for i in table:
            #checking for rows
            if sum(i)==3:
                winner=1
                game_over=True
                return[[70+0,70+x*120+60],[70+3*120,70+x*120+60]]
                #print("win")
            elif sum(i)==-3:
                winner=2
                game_over=True
                return[[70+0,70+x*120+60],[70+3*120,70+x*120+60]]
            #checking for columns
            if(table[0][x]+table[1][x]+table[2][x]==3):
                winner=1
                game_over=True
                return[[70+x*120+60,70+0],[70+x*120+60,70+3*120]]
            if(table[0][x]+table[1][x]+table[2][x]==-3):
                winner=2
                game_over=True
                return[[70+x*120+60,70+0],[70+x*120+60,70+3*120]]
            x+=1
            #now checking for diagonal
            if table[0][0]+table[1][1]+table[2][2]==3 or table[0][2]+table[1][1]+table[2][0]==3:
                winner=1
                game_over=True
                if table[0][0]+table[1][1]+table[2][2]==3:
                    return[[70,70],[70+360,70+360]]
                else:
                    return[[70,70+360],[70+360,70]]
                
            if table[0][0]+table[1][1]+table[2][2]==-3 or table[0][2]+table[1][1]+table[2][0]==-3:
                winner=2
                game_over=True
                if table[0][0]+table[1][1]+table[2][2]==-3:
                    return[[70,70],[70+360,70+360]]
                else:
                    return[[70,70+360],[70+360,70]]
            if turn==9:
                game_over=True
                winner=None
            #pygame.draw.line(screen,green,(70,70+(120/2)*(x+1)),(360+70,70+(120/2)*(x+1)),width=4)
        return[[0,0],[0,0]]

    
    pygame.init()

    # set the drawing window
    screen_width=500
    screen_height=500
    screen=pygame.display.set_mode([screen_width,screen_height])
    pygame.display.set_caption("Tic Tac Toe")
    player=1
    clicked=False
    running=True
    turn=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if game_over==False:
                if event.type ==pygame.MOUSEBUTTONDOWN and clicked ==False:
                    clicked=True
                if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                    clicked=False
                    pos=pygame.mouse.get_pos()
                    cell_x=(pos[0]-70)//120
                    cell_y=(pos[1]-70)//120
                    if (cell_x>=0 and cell_x<=2) and (cell_y>=0 and cell_y<=2) and table[cell_y][cell_x]==0:
                        table[cell_y][cell_x]=player
                        turn+=1
                        player=player*(-1)
                    #print(table)

        screen.fill((255,182,193))
        draw_grid(screen)
        pic_board(screen)
        coordinates=[[None,None],[None,None]]
        coordinates=check(turn)
        if game_over==True:
            pygame.draw.line(screen,(8,143,143),coordinates[0],coordinates[1],width=4)
            draw_winner(winner,screen)
            if event.type ==pygame.MOUSEBUTTONDOWN and clicked ==False:
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    print("hello")
                    table=[]
                    for x in range(3):
                        row=[0]*3
                        table.append(row)
                    pos=[]
                    player=1
                    winner=None
                    game_over=False
                    turn=0
        
        pygame.display.flip()
run_game()

    

