class ArtificialIntelligence():
    def __init__(self, p):
        self._piles=p
        pass
    def _goBinary(self):
        reminder=0
        exponent=0
        for i in self._piles.values():
            for y in range(0,4):
                if (i>=2**exponent):
                    reminder=i-2**exponent
                    i=reminder
                    print(reminder)
                    exponent-=1
                if exponent==0:
                    exponent=4
                
            # print(i)

    def winningStrategy(self):
        self._goBinary()
        pass
if __name__=="__main__":
    ai=ArtificialIntelligence({"A":19,"B":11,"C":1})
    ai._goBinary()