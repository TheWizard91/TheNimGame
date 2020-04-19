class ArtificialIntelligence():
    def __init__(self, p):
        self._piles=p
        pass
    def _goBinary(self):
        reminder=0
        exponent=4
        l=[]
        for i in self._piles.values():
            # print("in first iteration "+str(i))
            for y in range(0,5):
                if (i>=2**exponent):
                    print("in first if-----------------")
                    print("i: "+str(i))
                    # print("real exposnent:"+str(exponent))
                    e=2**exponent
                    # print("exponent number: "+str(e))
                    reminder=i-(e)
                    i=reminder
                    exponent-=1
                if (exponent==0):
                    print("in second if---------------------------")
                    print("i: "+str(i))
                    # print("real exposnent:"+str(exponent))
                    # print("exponent number: "+str(e))
                    exponent=4
                # print("in second iteration "+str(i))  
                exponent-=1
                l.append(i)
        print(l)

    def winningStrategy(self):
        self._goBinary()
        pass
    # this is now a rest
if __name__=="__main__":
    ai=ArtificialIntelligence({"A":19,"B":11,"C":1})
    ai._goBinary()
