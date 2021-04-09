class Character:
    def __init__(self):
        self.MAXHEALTH = 1000
        self.health = 1000
        self.level = 1
        self.alive = True
        self.experience = 0

    def deal(self, character, damage):
            if(character!=self):
                if(damage>character.health):
                    character.alive = False
                    character.health = 0
                else:
                    character.health-=damage

    def healing(self):
        if (self.alive == True) and (self.health < self.MAXHEALTH):
            #self.health += percent*MAXHEALTH
            self.health = self.MAXHEALTH

        if self.health > self.MAXHEALTH:
            self.health = self.MAXHEALTH

#Track B: Iteration 3
#A Character may Join or Leave one or more Factions.
#self.faction = [], self.append(Faction1) // self.remove(Faction2)
#Players belonging to the same Faction are considered Allies.
#Allies cannot Deal Damage to one another.
#Allies can Heal one another.

    def gainexperience (self,experience):
         if(experience > 0):
           self.experience+=experience
           if(self.experience>=(self.level+1)*(self.level+1)*10):
               self.level+=1
               self.experience=0
           if(self.level>100):
               self.level=100
