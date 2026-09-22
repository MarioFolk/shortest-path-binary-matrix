import unittest
from shortest_path_binary_matrix import Solution


class TestShortestPathBinaryMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_diagonal_move(self):
        grid = [[0, 1], [1, 0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), 2)

    def test_medium_grid(self):
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), 4)

    def test_blocked_start(self):
        grid = [[1, 0], [0, 0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), -1)

    def test_single_cell(self):
        grid = [[0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), 1)

    def test_no_path(self):
        grid = [[0, 1, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), -1)

    def test_all_open_3x3(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.sol.shortestPathBinaryMatrix(grid), 3)


if __name__ == "__main__":
    unittest.main()
