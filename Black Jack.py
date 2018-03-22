import random
import sys

dic = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 8, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10,'k': 10}
l=['A',2,3,4,5,6,7,8,9,10,'J','Q','k']

class bankroll:

    def __init__(self,account=0):
        self.account=account
        self.b=0

    def addbankroll(self):
        add = int(input("Enter Your Amount : "))
        self.account+=add

    def bet(self):
        self.val=int(input("Enter Your Bet : "))
        if(self.val>self.account):
            print("Your Bet is greater then the bankroll amount !\n try again :-\n")
            self.bet()
        else:
            self.b += self.val
            self.account -= self.val

    def winamount(self):
        return (self.account+(self.b*2))


class hand:

    def __init__(self,player1,player2):
        self.sum=0
        self.card=[]
        self.player1=player1
        self.player2=player2

    def hit(self):
        self.a = random.choice(l)
        if(self.a=='A'):
            self.checkA()
        else:
            self.sum += dic[self.a]
        self.card.append(self.a)

    def checkA(self):
        if((self.sum + 11) > 21):
            self.sum += dic[self.a]
        else:
            self.sum += 11

    def checktotal(self):
        if self.sum > 21:
            print("Dealer cards are :-\n",d.card)
            print("Dealer sum is : ",d.sum)
            print(self.player1," is Busted and ",self.player2,"wins !")
            if self.player2 is "Person":
                print("Your Total Money is now : ", x.winamount())
            Playagain()
        elif self.sum == 21 :
            print("Dealer cards are :-\n",d.card)
            print("Dealer sum is : ",d.sum)
            print(self.player1,"Wins !")
            if self.player1 is "Person":
                print("Your Total Money is now : ", x.winamount())
            Playagain()
def startgame():

    print("**Welcome To The Black Jack game !**\n")
    x.addbankroll()
    x.bet()
    d.hit()
    d.hit()
    p.hit()
    p.hit()
    print("Dealer first Card is :-\n ", d.card[0])
    print("Your Cards are :-\n ", p.card)
    print("\nYour Sum is: ",p.sum)
    p.checktotal()
    agame()

def agame():
    while True :
        print("-> Please Choose One Option :-\n")
        print("1.Hit\n2.Stand\n3.More Bet\n4.Add Money\n5.Total Bet\n6.Remain Money")
        n = int(input("\nEnter Your Choice : "))
        if n is 1:
            p.hit()
            if d.sum < 17 :
                d.hit()
            print("\nYour Cards are :-\n ", p.card)
            print("\nYour Sum : ",p.sum)
            p.checktotal()
            d.checktotal()
        elif n is 2:
            print("Your Cards are :-\n ", p.card)
            print("\n Your Sum is: ",p.sum)
            print("\nDealer cards are :-\n",d.card)
            print("\nDealer sum is : ",d.sum)
            if d.sum == p.sum :
                print("The Game Is Draw !")
            elif d.sum > p.sum :
                print(p.player2," Wins !")
            else:
                print(p.player1, " Wins !")
                print("Your Total Money is now : ", x.winamount())
            Playagain()
        elif n is 3 :
            x.bet()

        elif n is 4 :
            x.addbankroll()

        elif n is 5 :
            print("Your Total Bet Is : ",x.b)

        else:
            print("The Remain Amount Is : ",x.account)

def Playagain():
    r=input("\n Enter Y For play again or N for Exit :" )
    if r is 'y' or r is 'Y' :
        p.card=[]
        d.card=[]
        p.sum=0
        d.sum=0
        x.account=0
        x.b=0
        startgame()
    else:
        sys.exit("Thank You !")




x=bankroll()
p=hand("Person","Dealer")
d=hand("Dealer","Person")
startgame()