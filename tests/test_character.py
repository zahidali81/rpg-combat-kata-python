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

