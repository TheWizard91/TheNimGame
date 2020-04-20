class ArtificialIntelligence():
    def __init__(self, p):
        """Computer playing the game agianst player1
        pre: p dictionary of piles and their values.
        post:---"""

        self._piles=p
        print(self._piles, self._piles.values())
        pass

    def _goBinary(self):
        """Get the binary representation of values in each pile"""
        c=0
        reminder=0
        exponent=4
        twoRaiseToexponent=2**exponent
        dictionaryOfBaseRasedToPowers={"16":0,"8":0,"4":0,"2":0,"1":0}
        # tuppleOfBaseRasedToPowers=(16,8,4,2,1)
        
        for i in self._piles.values():
            for y in range(0,5):
                if (i>=twoRaiseToexponent):
                    # valueInTupple=tuppleOfBaseRasedToPowers[y]*NOT NEEDED
                    dictionaryOfBaseRasedToPowers[str(twoRaiseToexponent)]+=1
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

        print(dictionaryOfBaseRasedToPowers)
        # print(self._piles)
    def winningStrategy(self):
        """Strategy to which the computer will beat the opponent."""
        
        self._goBinary()
        pass
    # this is now a rest
if __name__=="__main__":
    ai=ArtificialIntelligence({"A":19,"B":11,"C":1})#, "D":15, "E":10, "G":5})
    ai._goBinary()
