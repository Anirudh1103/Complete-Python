def takeIP():
    player1 = int(input("Snake(1), Water(-1) or Gun(0): "))
    player2 = int(input("Snake(1), Water(-1) or Gun(0): "))
    SnakeWaterGun(player1,player2)

def SnakeWaterGun(p1,p2):
    if(p1 == p2):
        print(" Draw \n Play again ")
        takeIP()
    elif((p1 == 1 and p2 == -1) or (p1 == -1 and p2 == 1)):
        print("Snake wins!!!")
    elif((p1 == -1 and p2 == 0) or (p1 == 0 and p2 == -1)):
        print("Water wins!!!")
    elif((p1 == 0 and p2 == 1) or (p1 == 1 and p2 == 0)):
        print("Gun wins!!!")
    
    
takeIP()