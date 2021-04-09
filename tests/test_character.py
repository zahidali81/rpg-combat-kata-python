import pytest
from rpg_combat_kata.character import Character

class TestCharacter:

    def test_health(self):
        character = Character()
        assert character.health == 1000

    def test_level(self):
        character = Character()
        assert character.level == 1

    def test_alive(self):
        character = Character()
        assert character.alive == True

    def test_damage(self):
        character1 = Character()
        character2 = Character()
        character1.deal(character2, 500)
        assert character2.health == 500
        assert character2.alive == True

    def test_self_damage(self):
        character = Character()
        character.deal(character, 100)
        assert character.health == 1000
        assert character.alive == True

    def test_big_damage(self):
        character1 = Character()
        character2 = Character()
        character1.deal(character2, 2000)
        assert character2.health == 0
        assert character2.alive == False

    def test_negative_damage(self):
        character1 = Character()
        character2 = Character()
        character1.deal(character2, -100)
        assert character2.health == 1100
        assert character2.alive == True

    def test_heal(self):
        character = Character()
        character.health = 500
        character.healing()
        assert character.health == 1000

    def test_heal_dead(self):
        character = Character()
        character.alive = False
        character.health = 0
        character.healing()
        character.alive = False
        assert character.health == 0

    def test_initial_experience(self):
        character = Character()
        assert character.experience == 0

    def test_gain_experience(self):
        character = Character()
        character.gainexperience(20)
        assert character.experience == 20
        assert character.level == 1

    def test_level_up(self):
        character = Character()
        character.gainexperience(50)
        assert character.level == 2
        assert character.experience == 0

    def test_max_level(self):
        character = Character()
        for i in range(120):
            character.gainexperience(100*100*10)
        assert character.level == 100

    def test_negative_exp(self):
        character = Character()
        character.gainexperience(-10)
        assert character.level == 1
        assert character.experience == 0
