from unittest import TestCase, main

from cube import Color, Cube, CubeSide, Move, Plane


class TestMove(TestCase):
    def test_reverse(self):
        move_cases = [Move(0, Plane.X, True), Move(1, Plane.Z, False)]
        for m in move_cases:
            rev = m.reverse()
            self.assertEqual(m.idx, rev.idx)
            self.assertEqual(m.plane, rev.plane)
            self.assertNotEqual(m.clockwise, rev.clockwise)

    def test_random_move(self):
        m = Move.random_move(3)
        self.assertIsNotNone(m)

    def test_str(self):
        m = Move(1, Plane.Y, True)
        self.assertEqual(str(m), "Move rotated Plane.Y 1 index clockwise")


class TestCubeSide(TestCase):
    def test_rotate_reversible(self):
        c = CubeSide("test", 3, Color.RED)
        # Manually alter the sides
        c.state[0][0] = Color.BLUE
        c.state[1][1] = Color.GREEN
        c.state[2][2] = Color.YELLOW

        # Test full rotation both ways
        init_copy = c.state.copy()
        for _ in range(4):
            c.rotate(True)
        self.assertEqual(c.state, init_copy)
        for _ in range(4):
            c.rotate(False)
        self.assertEqual(c.state, init_copy)

        # Test single rotation
        c.rotate(True)
        self.assertEqual(c.state[0][0], Color.RED)
        self.assertEqual(c.state[0][1], Color.RED)
        self.assertEqual(c.state[0][2], Color.BLUE)
        self.assertEqual(c.state[1][0], Color.RED)
        self.assertEqual(c.state[1][1], Color.GREEN)
        self.assertEqual(c.state[1][2], Color.RED)
        self.assertEqual(c.state[2][0], Color.YELLOW)
        self.assertEqual(c.state[2][1], Color.RED)
        self.assertEqual(c.state[2][2], Color.RED)

        # rotate backwards
        c.rotate(False)
        self.assertEqual(c.state[0][0], Color.BLUE)
        self.assertEqual(c.state[0][1], Color.RED)
        self.assertEqual(c.state[0][2], Color.RED)
        self.assertEqual(c.state[1][0], Color.RED)
        self.assertEqual(c.state[1][1], Color.GREEN)
        self.assertEqual(c.state[1][2], Color.RED)
        self.assertEqual(c.state[2][0], Color.RED)
        self.assertEqual(c.state[2][1], Color.RED)
        self.assertEqual(c.state[2][2], Color.YELLOW)

    def test_get_row(self):
        c = CubeSide("test", 3, Color.RED)
        # Manually alter the sides
        c.state[0][0] = Color.BLUE
        c.state[1][1] = Color.GREEN
        c.state[2][2] = Color.YELLOW

        self.assertEqual(c.get_col(0), [Color.BLUE, Color.RED, Color.RED])
        self.assertEqual(c.get_col(1), [Color.RED, Color.GREEN, Color.RED])
        self.assertEqual(c.get_col(2), [Color.RED, Color.RED, Color.YELLOW])

        self.assertEqual(c.get_row(0), [Color.BLUE, Color.RED, Color.RED])
        self.assertEqual(c.get_row(1), [Color.RED, Color.GREEN, Color.RED])
        self.assertEqual(c.get_row(2), [Color.RED, Color.RED, Color.YELLOW])


class TestCube(TestCase):
    def test_full_plane_rotation(self):
        c = Cube()
        for clock_dir in (True, False):
            for p in list(Plane):
                for idx in range(c.size):
                    m = Move(idx, p, clock_dir)
                    self.assertTrue(c.solved())
                    for n in range(4):
                        c.rotate(m)
                        if n < 3:
                            self.assertFalse(c.solved())
                    self.assertTrue(c.solved)

    def test_all_actions_reversible(self):
        c = Cube()
        chains = (1, 2, 3)
        for chain in chains:
            for clock_dir in (True, False):
                for p in list(Plane):
                    for idx in range(c.size):
                        m = Move(idx, p, clock_dir)
                        self.assertTrue(c.solved())
                        for _ in range(chain):
                            c.rotate(m)
                        self.assertFalse(c.solved())
                        for _ in range(chain):
                            c.rotate(m.reverse())
                        self.assertTrue(c.solved())

    def test_move_chaining(self):
        moves = [
            Move(2, Plane.Z, True),
            Move(1, Plane.Z, False),
            Move(2, Plane.Y, True),
            Move(0, Plane.X, False),
        ]

        rev = [m.reverse() for m in moves]

        for n in range(1, len(moves) + 1):
            c = Cube()
            for i in range(n):
                c.rotate(moves[i])
            self.assertFalse(c.solved())
            for i in rev[:n][::-1]:
                c.rotate(i)
            self.assertTrue(c.solved())

    def test_many_fail(self):
        moves = [
            Move(1, Plane.X, False),
            Move(2, Plane.X, False),
            Move(2, Plane.Z, False),
            Move(0, Plane.X, False),
            Move(1, Plane.Y, False),
        ]

        rev = [m.reverse() for m in moves]

        c = Cube()
        for i in range(len(moves)):
            c.rotate(moves[i])
        for i in rev[::-1]:
            c.rotate(i)
        self.assertTrue(c.solved())


class TestRandomCube(TestCase):
    # Note: These test cases rely on randomization and are non-deterministic

    def test_many_reversible(self):
        c = Cube()
        many_moves = [Move.random_move(c.size) for _ in range(5000)]
        for m in many_moves:
            c.rotate(m)
        reverse_all = [m.reverse() for m in many_moves]
        # apply in reverse order
        reverse_all.reverse()
        for r in reverse_all:
            c.rotate(r)
        self.assertTrue(c.solved())


    def test_print(self):
        c = Cube()
        c.print()


if __name__ == "__main__":
    main()
