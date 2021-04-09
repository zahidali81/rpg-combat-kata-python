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
