from project.hero import Hero

from unittest import TestCase, main

class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("Gosho", 5, 100.0, 15.0)
        #self.enemy_hero = Hero("Pencho", 3, 50.0, 10.0)

    def test_hero_init(self):
        self.assertEqual("Gosho", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

    def test_hero_battle_if_battle_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))
    
    def test_hero_battle_if_health_is_negative(self):
        self.hero = Hero("Gosho", 5, 0, 15.0)
        self.enemy_hero = Hero("Pencho", 3, 50.0, 10.0)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
    
    def test_hero_battle_if_enemy_health_is_negative(self):
        self.enemy_hero = Hero("Pencho", 3, 0, 25.0)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Pencho. He needs to rest", str(ex.exception))

    def test_hero_battle_if_you_win(self):
        self.enemy_hero = Hero("Pencho", 3, 50.0, 10.0)
        self.assertEqual("You win", str(self.hero.battle(self.enemy_hero)))
        self.assertEqual(75.0, self.hero.health)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(20.0, self.hero.damage)
        self.assertEqual(-25.0, self.enemy_hero.health)

    def test_hero_battle_if_draw(self):
        self.enemy_hero = Hero("Pencho", 3, 50.0, 35.0)
        self.assertEqual("Draw", str(self.hero.battle(self.enemy_hero)))
        self.assertEqual(-5.0, self.hero.health)
        self.assertEqual(-25.0, self.enemy_hero.health)

    def test_hero_battle_if_you_lose(self):
        self.hero = Hero("Gosho", 5, 100.0, 5.0)
        self.enemy_hero = Hero("Pencho", 3, 50.0, 35.0)
        self.assertEqual("You lose", str(self.hero.battle(self.enemy_hero)))
        self.assertEqual(-5.0, self.hero.health)
        self.assertEqual(30.0, self.enemy_hero.health)
        self.assertEqual(40.0, self.enemy_hero.damage)
        self.assertEqual(4, self.enemy_hero.level)

    def test_hero_str_dunder(self):
        expected_result = "Hero Gosho: 5 lvl\nHealth: 100.0\nDamage: 15.0\n"
        self.assertEqual(expected_result, str(self.hero.__str__()))

if __name__ == "__main__":
    main()