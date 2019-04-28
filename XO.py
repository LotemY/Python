import os

def matPrint(arr):
    caseBord="---------------"
    print(caseBord,end="   ")
    print("X=",xWinCount,"  O=",oWinCount)
    for i in range(0,3):
        for j in range(0,3):
            print("|",arr[i][j],end=" |")
        print()
    print(caseBord)

def occupied(choice):
    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j]==choice:
                return 1
    return 0
            

def correct(choice):
    while choice<1 or choice>9:
        print("Invalid number (1-9)",end=": ")
        choice=(int)(input())
        print()
    return choice

def winCheck():
    rowCount=0
    colCount=0
    priCrossCount=0
    secCrossCount=0
    for i in range(0,3):
        rowCount=0
        colCount=0
        for j in range(0,2):
            row=arr[i][j]
            if row==arr[i][j+1]:
                rowCount+=1
                if rowCount==2:
                    return arr[i][j]
            else:
                rowCount=0
            
            col=arr[j][i]
            if col==arr[j+1][i]:
                colCount+=1
                if colCount==2:
                    return arr[j][i]      
            else:
                colCount=0  
        
        for p in range(0,3):
            priCross=arr[0][0]
            secCross=arr[0][2]
            if i==p and priCross==arr[i][p]:
                priCrossCount+=1
                if priCrossCount==3:
                    return arr[i][p]
            if i+p==2 and secCross==arr[i][p]:
                secCrossCount+=1
                if secCrossCount==3:
                    return arr[i][p]
    return 0


player="X"
win=0
count=0
xWinCount=0
oWinCount=0
arr=[[1,2,3],[4,5,6],[7,8,9]]

choice=0

while win==0:
    if count==0:
        os.system('cls')
        matPrint(arr)
    ok=0
    count+=1   
    
    print("Player",player,end=" choose number: ")
    choice=(int)(input())
    print()

    choice=correct(choice)

    while ok==0:
        ok=occupied(choice)
        if ok==0:
            print("This place is occupied please choose a new one:",end=" ")
            choice=(int)(input())
            choice=correct(choice)

    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j]==choice:
                arr[i][j]=player

    os.system('cls')
    matPrint(arr)

    if count>4:
        win=winCheck()
        if win=="X":
            xWinCount+=1
            win=1
            os.system('cls')
            matPrint(arr)
            print("X Wins")
            

        if win=="O":
            oWinCount+=1
            win=1
            os.system('cls')
            matPrint(arr)
            print("O Wins")
            

    if count==9 and win==0:
        print("Draw")

    if player=="X":
        player="O"
    else:
        player="X"

    if win==1 or count==9:
        print("Do you want a rematch?",end="... (press 1 for Yes, 0 for No) ")
        rematch=(int)(input())

        while rematch<0 or rematch>1:
            print ("Sorry I didn't get it (press 1 for Yes, 0 for No)",end=" ")
            rematch=(int)(input())
        
        if rematch==0:
            print("Bye Bye :)")
            break
        else:
            player="X"
            win=0
            count=1
            for w in range(0,3):
                for z in range(0,3):
                    arr[w][z]=count
                    count+=1
            count=0

            



