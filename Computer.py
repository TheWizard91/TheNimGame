class ArtificialIntelligence():
    def __init__(self, p):
        """Computer playing the game agianst player1
        pre: p dictionary of piles and their values.
        post:---"""

        self._piles=p
        self._dictionaryOfBaseRasedToPowers={"16":0,"8":0,"4":0,"2":0,"1":0}
        self._boardIsInBalance=False
        self._nimSum=0


    def _goBinary(self):
        """Get the binary representation of values in each pile"""
        c=0
        reminder=0
        exponent=4
        twoRaiseToexponent=2**exponent
        # tuppleOfBaseRasedToPowers=(16,8,4,2,1)
        
        for i in self._piles.values():
            for y in range(0,5):
                if (i>=twoRaiseToexponent):
                    # valueInTupple=tuppleOfBaseRasedToPowers[y]*NOT NEEDED
                    self._dictionaryOfBaseRasedToPowers[str(twoRaiseToexponent)]+=1
                    
                    # print(dictionaryOfBaseRasedToPowers[str(valueInTupple)])
                    # print(i)
                    reminder=i-(twoRaiseToexponent)
                    i=reminder
                if (exponent==0):
                    exponent=5
                c+=1
                exponent-=1
                twoRaiseToexponent=2**exponent
                print("c: "+str(c))

        print(self._dictionaryOfBaseRasedToPowers)
        print(self._piles)

    def setNimSum(self):
        """"""

        for i in self._dictionaryOfBaseRasedToPowers.val():
            self._nimSum+=i

    def getNimSum(self):
        """"""
        return self._nimSum

    def isTheBoardBalanced(self):
        """"""
        if ((self._nimSum%2)==0):
            self._boardIsInBalance=True
    
    def winningStrategy(self):
        """Strategy to which the computer will beat the opponent."""
        
        # Go binary to see the board configuration
        self._goBinary()
        # Set the nim sum
        self.setNimSum()
        # See if the board in balance
        # if it is, then the player is is
        # losing position else winning
        self.isTheBoardBalanced()
        
        pass
    # this is now a rest
if __name__=="__main__":
    ai=ArtificialIntelligence({"A":19,"B":11,"C":1})#, "D":15, "E":10, "G":5})
    ai._goBinary()