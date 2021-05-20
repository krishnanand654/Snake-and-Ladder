import random
from packages import mod1

user=0
temp1=0
temp2=0
dice=0
x=0
class player:
        
    def x(self):
        global user
        global dice
        n=input("do u want to roll the dice y/n : ")
        if n=='y':
            dice=mod1.dicer()
            user=user+dice
            print("dice=",dice)
            x=0
        if n=='n':
            exit()
        return dice
                    
                    
    def ladder(self,temp):
        global i
        if temp==2:
            temp=38
            print(" \n\n ''''hurray... : you got the ladder'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==4:
            temp=14
            print(" \n\n '''''hurray... : you got the ladder'''''\n\n current location = ",temp,"\n\n")
            return temp  
        if temp==9:
            temp=31
            print(" \n\n '''''hurray... : you got the ladder''''' \n\n current location = ",temp,"\n\n")
            return temp  
        if temp==21:
            temp=42
            print(" \n\n '''''hurray... : you got the ladder '''''\n\n current location = ",temp,"\n\n")
            return temp  
        if temp==28:
            temp=84
            print(" \n\n '''''hurray... : you got the ladder'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==51:
            temp=67
            print(" \n\n '''''hurray... : you got the ladder'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==72:
            temp=91
            print(" \n\n '''''hurray... : you got the ladder'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==80:
            temp=99
            print(" \n\n '''''hurray... : you got the ladder'''''\n \n current location = ",temp,"\n\n")
            return temp   
                   
    def snake(self,temp):
        global j
        if temp==17:
            temp=7
            print("\n\n '''''caught by the snake''''' \n\n current location = ",temp,"\n\n")
            return temp
        if temp==54:
            temp=34
            print("\n\n''''' caught by the snake'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==63:
            temp=19
            print("\n\n '''''caught by the snake'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==64:
            temp=60
            print("\n\n '''''caught by the snake'''''\n \n current location = ",temp,"\n\n")
            return temp
        if temp==87:
            temp=36
            print("\n\n '''''caught by the snake'''''\n\n current location = ",temp,"\n\n")
            return temp
        if temp==93:
            temp=73
            print("\n\n'''''caught by the snake'''''\n\n current location = ",temp,"\n\n")
            return temp
        if temp==95:
            temp=75
            print("\n\n '''''caught by the snake''''' \n current location = ",temp,"\n\n")
            return temp
        if temp==98:
            temp=79
            print("\n\n '''''caught by the snake''''' \n current location = ",temp,"\n\n")
            return temp
        
        
    def constraint(self,temp):
        if(temp>=100):
            temp=99
            print("""\n\ncurrent location= 99
                         You are one step away from success only number
                         '1' can help you to step onto 100 \n\n\n\n""")
        if(temp==99 and dice==1):
            global temp1
            global temp2
            if temp1>temp2:
                temp1=100
            else:
                temp2=100
            temp=100
            f=open('won.txt','r+')
            print(f.read())
            f.close()
            if temp1==100:
                k=open('data.txt','w')
                k.write(str(player1)+" won")
                k.close()
            if temp2==100:
                k=open('data.txt','w')
                k.write(str(player2)+" won")
                k.close()
            x=input("\n\n\n\n\npress e to exit :")
            if x=='e':
                exit()
        return temp
            
   
             
                   
 
lst=[2,4,9,21,28,51,72,80]
lst1=[17,54,63,64,87,93,95,98]
j=open('rule.txt','r')
print(j.read())
j.close()
player1=input("Enter name of player 1 : ")
player2=input("Enter name of player 2 : ")
while 1:
#user1
    p1=player()
    print("\n\n\t\t\t\t",player1,"\n\n")
    p1.x()
    temp1=temp1+user
    if temp1<=99:
        print("current location = ",temp1)
    if  temp1 in lst:
        temp1=p1.ladder(temp1)
    if temp1 in lst1:
       temp1=p1.snake(temp1)
    p1.constraint(temp1)
    user=0
  #user2
    p2=player()
    print("\n\n\t\t\t\t",player2,"\n\n")
    p2.x()
    temp2=temp2+user
    if temp2<=99:
        print("current location=",temp2)
    if  temp2 in lst:
        temp2=p2.ladder(temp2)
    if temp2 in lst1:
        temp2=p2.snake(temp2)
    p2.constraint(temp2)
    user=0
    if temp1>temp2:
        print("\n\n\t\t\t\t(",player1," leads)")
    elif temp1==99 and temp2==99:
        print("\n\n\t\t\t\t(",player1 ,"and ",player2 ,"are both in 99")
    else:
        print("\n\n\t\t\t\t(",player2," leads)")
    
    
    
        
        
    

        
            
