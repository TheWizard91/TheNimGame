class Nim():
    def __init__(self):

        """This is the class where the set up is being made""" 
        
        self._pilesAndStones = {}
        self._player1 = ""
        self._player2 = ""
        self._numberOfPiles = 0
        self._currentPlayer=""

    def setName(self, name, one=True):
        """Set the username
        pre: n is a string.
        post: setting player to name."""
        if(one):
            self._player1=name
        else:
            self._player2=name

    def getPlayer(self, player):
        """Return player
        pre:player is string
        post:---"""
        if(player==1):
            return self._player1
        else:
            return self._player2
    # def _setPilesHelper(self, n):
    #     """Set number of piles for the game.
    #     pre: n is a int.
    #     post: return n."""
    #     return n
    def _sertCurretPlayerHelperCheckInputRnage(self):

        """Helper method of setCurrentPlayer, it chooses the player that will start the game."""
        
        player1Input=int(input(self._player1+" Enter 1 for s 2 for p and 3 for r: "))
        player2Input=int(input(self._player2+" Enter 1 for s 2 for p and 3 for r: "))

        while(True):
            if((1<=player1Input<=3) and (1<=player2Input<=3)):
                break
            if((1>player1Input) or (player1Input>3)):
                player1Input=int(input(self._player1+" Enter 1 for s 2 for p and 3 for r: "))
            if((1>player1Input) or (player2Input>3)):
                print("in else")
                player2Input=int(input(self._player2+" Enter 1 for s 2 for p and 3 for r: "))

        return player1Input, player2Input
        
    def setCurrentPlayer(self):

        """Setting the player that will start the game."""
        
        player1Input, player2Input = self._sertCurretPlayerHelperCheckInputRnage()
        
        # Cheking player's input
        while(player1Input==player2Input):
            print("redo because you are even")
            player1Input=int(input(self._player1+" Enter 1 for s 2 for p and 3 for r: "))
            player2Input=int(input(self._player2+" Enter 1 for s 2 for p and 3 for r: "))
        
        # Setting up first player to start the game.
        if(player1Input==1 and player2Input):
            self._currentPlayer=self._player1
        if(player1Input==1 and player2Input==3):
            self._currentPlayer=self._player2
        if(player1Input==2 and player2Input==1):
            self._currentPlayer=self._player2
        if(player1Input==2 and player1Input==3):
            self._currentPlayer=self._player1

    def getCurrentPlayer(self):
        
        """Return the current player"""

        return self._currentPlayer

    def switchPlayer(self):
        
        """Switching the player's turns"""
        
        if(self._currentPlayer==self._player1):
            self._currentPlayer = self._player2
        else:
            self._currentPlayer=self._player1

    def setNumberOfPiles(self):

        """Set the stones to pile x"""

        self._numberOfPiles = int(input(self._currentPlayer+"enter the number of piles that you want in the game: "))

    def setPiles(self):
        
        """Setting piles."""
        
        pile=65
        # print("in set piles")
        for i in range(0,self._numberOfPiles):
            self._pilesAndStones[chr(pile+i)]=0
        # print(self._pilesAndStones)
                
    def setStones(self):
        
        """Set the stones in piles."""
        
        pile=65
        print(self._pilesAndStones)
        for i in self._pilesAndStones:
            self._pilesAndStones[i]= int(input(self._currentPlayer+
                                                " enter number of stoens for plie "+
                                                i+": "))
    def getPliesAndStones(self):
        
        """Get dictionary containing the piles along side the stones."""
        
        return self._pilesAndStones

    # def choosePileToTakeWayFrom(self):
    #     """Choose te file to take away from"""
    #     chosePile=input(self._currentPlayer+" enter pile to take away from")

    def _getChosenPileToTakeWayFrom(self):
        
        """Helper of subtractStonesFromChoosenPiles, get the pile that is choosen"""
        
        chosePile=input(self._currentPlayer+" enter pile to take away from: ").upper()
        
        # Checing User's input(i.e."You need to input a letter A<=x<=E")
        while(True):
            if(chosePile not in self._pilesAndStones.keys()):
                print("You need to input a letter A to "+chr(65+self._numberOfPiles-1))
                chosePile=input(self._currentPlayer+" enter pile to take away from: ").upper()
            else:
                break
        return chosePile

    def _chooseStonesTotakeWayFrom(self, pile):
        
        """Helper of subtractStonesFromChoosenPiles, get the number of piles to subtract from.
        pre:pile is a strong.
        post:---"""
        
        numberOfStones=int(input(self._currentPlayer+" enter the number of stoned to take away from "+pile+": "))
        
        # Cehck use's input
        while(True):
            if(self._pilesAndStones[pile]==0):
                print("there are no stones on pile: "+chr(self._pilesAndStones[pile])+" so choose another")
            if(self._pilesAndStones[pile]<numberOfStones):
                print("Your entry is bigger than the number of available stones in pile: "+ chr(self._pilesAndStones[pile]))
                numberOfStones=int(input(self._currentPlayer+" enter the number of stoned to take away from "+pile+": "))
            if(numberOfStones<0):
                print("Number eneterd is a negative cannot happen")
                numberOfStones=int(input(self._currentPlayer+" enter the number of stoned to take away from "+pile+": "))
            if(numberOfStones==0):
                print("Number enetered is zero cannot have that")
                numberOfStones=int(input(self._currentPlayer+" enter the number of stoned to take away from "+pile+": "))
            else:
                break
        
        return numberOfStones

    def subtractStonesFromChosenPile(self):
        
        """"Take away n stones"""
        
        pile=self._getChosenPileToTakeWayFrom()
        stones=self._chooseStonesTotakeWayFrom(pile)
        self._pilesAndStones[pile]=self._pilesAndStones[pile]-stones
        # print(self._pilesAndStones)

    def _gameOverHelperFindSumOfAllValue(self):
        
        """Helper of gameOver() calculate the sum."""
        
        sum=0
        pile=65
        
        for i in range(0,self._numberOfPiles):
            sum+=self._pilesAndStones[chr(pile+i)]
        
        return sum

    def getSum(self):
        
        """Helper of gameOver() get the sum of all piles."""
        
        return self._gameOverHelperFindSumOfAllValue()

    def gameOver(self):
        
        """States when the game is over."""
        
        sum=self._gameOverHelperFindSumOfAllValue()
        
        if(sum==0):
            if(self._currentPlayer==self._player1):
                print(self._player1+" has won")
            else:
                print(self._player2+" has won")

if __name__ == "__main__":
    # Start game
    nim = Nim()
    # Get users names
    p1=input("p1 enter name: ")
    p2=input("p2 enter name: ")
    # Set those names
    nim.setName(p1)
    nim.setName(p2, False)
    # Set current player
    nim.setCurrentPlayer()
    # The current player gets to set the piles and stones
    # currentPlayer=nim.getCurrentPlayer()
    nim.setNumberOfPiles()
    nim.setPiles()
    nim.setStones()
    sum=nim.getSum()
    # print(nim._pilesAndStones)
    # print(sum)
    while(True):
        sum=nim.getSum()
        if(sum!=0):
            print(sum)
            nim.subtractStonesFromChosenPile()
            nim.switchPlayer()
            # sum=nim.getSum()
        else:
            # Change the player to get to the right one
            # TO DO the fix algorithm so that I do not have to switch player. 
            nim.switchPlayer()
            break
    nim.gameOver()


