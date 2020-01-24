class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,name):
        self.name = name

    def party(self):
        self.x = self.x + 1
        print("x value",self.x)




class FootballFan(PartyAnimal):
    partypoints = 0;

    def touchdown(self):
        self.partypoints = self.partypoints +7
        self.party()
        print("Name is",self.name,"Party points",self.partypoints)



an = PartyAnimal("Umar")
an.party()
an.party()
an.party()


an = FootballFan("Umar")
an.touchdown()
