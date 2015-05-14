#!/usr/bin/env python3

import unittest
import figure as fg
import game as gm


class Test(unittest.TestCase):

    def test_create_game(self):
        game = gm.Game()
        self.assertIsNotNone(game)

    def test_fall_down(self):
        game = gm.Game()
        self.assertEqual(game.current.y + len(game.current.figure), 0)
        game.current.fall_down(game)
        self.assertEqual(game.current.y + len(game.current.figure), 1)

    def test_del_rows(self):
        game = gm.Game()
        game.level[-1] = [1] * gm.WIDTH
        game.del_rows()
        self.assertEqual(game.level[-1], [0]*gm.WIDTH)
        self.assertEqual(game.score, gm.WIDTH)

    def test_highscore(self):
        game = gm.Game()
        game.score = 10
        game.stop()
        self.assertEqual(game.highscore, 10)

    def test_fell_down(self):
        game = gm.Game()
        self.assertEqual(game.level[-1], [0] * gm.WIDTH)
        game.current.y = gm.HEIGHT - len(game.current.figure)
        game.current.fall_down(game)
        self.assertNotEqual(game.level[-1], [0] * gm.WIDTH)

    def test_rotate(self):
        game = gm.Game()
        game.current.figure = [[1],[1],[1],[1],[1]]
        game.current.x = 0
        game.current.y = 0
        game.current.rotate(game.level)
        game.fix_current()
        self.assertEqual([1] * 5 + [0] * (gm.WIDTH - 5), game.level[2])

if __name__ == '__main__':
    unittest.main()
