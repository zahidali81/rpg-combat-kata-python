class Character:
    health = 1000
    level = 1
    alive = True

    def deal(self, character, damage):
        if(character!=self):
            if(damage>character.health):
                character.alive = False
                character.health = 0
            else:
                character.health-=damage
