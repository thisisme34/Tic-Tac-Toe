import sys
list=[0,1,2,3,4,5,6,7,8]
def display():
    i=0
    while(i<=8):
        for j in range(0,3):
            print(list[i],end="  ")
            i+=1
        print("\n")
def game(p1="player 1",p2="player 2"):
    if ((list[0]==list[1] ==list[2]=="O") or (list[3]==list[4] ==list[5]=="O") or (list[6]==list[7] ==list[8]=="O")or(list[0]==list[4] ==list[8]=="O")or(list[2]==list[4] ==list[6]=="0")or
    (list[0]==list[3] ==list[6]=="O") or(list[1]==list[4] ==list[7]=="O") or (list[2]==list[5] ==list[8]=="O")  ):
        print(f"{p1} wins")
        sys.exit(0)
    elif ((list[0]==list[1] ==list[2]=="X") or (list[3]==list[4] ==list[5]=="X") or (list[6]==list[7] ==list[8]=="X")or(list[0]==list[4] ==list[8]=="X")or(list[2]==list[4] ==list[6]=="X")or
    (list[0]==list[3] ==list[6]=="X") or(list[1]==list[4] ==list[7]=="X") or (list[2]==list[5] ==list[8]=="X")  ):
        print(f"{p2} wins")
        sys.exit(0)
    


        

player_1=input("enter your name player 1 for O ")
player_2=input("enter you name player 2 for X ")
display()
for i in range(0,18):
    num=int(input(f"enter your choice {player_1} "))
    while 1:
        if((num>8) or (num<0) or list[num]=="O" or list[num]=="X"):
            print("please enter a valid choice")
            num=int(input(f"enter your choice {player_1} "))
        else :
            list[num]="O"
            game(player_1,player_2)
            display()
            break

    while 1 :
        num=int(input(f"enter your choice {player_2} "))
        if( (num>8)or(num<0) or list[num]=="O" or list[num]=="X"):
            print("please enter a valid choice")
            num=int(input(f"enter your choice {player_2} "))
        else :
            list[num]="X"
            game(player_1,player_2)
            display()
            break
print("it is a tie")
        







