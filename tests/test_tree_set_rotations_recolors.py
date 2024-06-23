"""Module with the tests for the TreeSet class rotations and recolors."""

import unittest
from model.tree_set import *


class TestsTreeSetRotationsAndRecolors(unittest.TestCase):
    """Test class for the TreeSet class rotations and recolors."""

    def setUp(self):
        """Set up the test class."""
        self.tree = TreeSet(int)

    def test_first_element_black_int(self):
        """Test first node in the tree black."""
        self.tree.add(1)
        self.assertEqual(self.tree._RedBlackTree__get_color(1), RedBlackTree._BLACK)

    def test_right_child_red_int(self):
        """Test right child of root in the tree red."""
        self.tree.add(2)
        self.tree.add(3)
        self.assertEqual(self.tree._RedBlackTree__get_color(3), RedBlackTree._RED)

    def test_left_child_red_int(self):
        """Test left child of root in the tree red."""
        self.tree.add(2)
        self.tree.add(1)
        self.assertEqual(self.tree._RedBlackTree__get_color(1), RedBlackTree._RED)

    def test_root_recolor_int(self):
        """Test recolor of the root when in is changed."""
        self.tree.add(1)
        self.assertEqual(self.tree._RedBlackTree__get_color(1), RedBlackTree._BLACK)
        self.tree.add(2)
        self.tree.add(3)
        self.assertEqual(self.tree._RedBlackTree__get_color(1), RedBlackTree._RED)

    def test_left_rotation_recolor_int(self):
        """Test nodes recolors and propagations when a new node is inserted."""
        self.tree.add_all([1, 2, 3, 4, 5, 6, 7])
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._BLACK, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED]
        self.tree.add(8)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._BLACK, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._BLACK, RedBlackTree._RED]
        self.assertEqual(tree_colors, real_colors)

    def test_right_rotation_recolor_int(self):
        """Test nodes recolors and propagations when a new node is inserted."""
        self.tree.add_all([8, 7, 6, 5, 4, 3, 2])
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED, RedBlackTree._RED,
                       RedBlackTree._BLACK, RedBlackTree._BLACK,
                       RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)
        self.tree.add(1)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._BLACK,
                       RedBlackTree._RED, RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_case_4_1_int(self):
        """Test Case 4: Uncle is red and the violator node is in external position."""

        self.tree.add_all([10, 5, 15, 3, 7])
        self.tree.add(2)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_case_4_2_int(self):
        """Test Case 4: Uncle is red and the violator node is in internal position."""

        self.tree.add_all([10, 5, 15, 3, 7])
        self.tree.add(4)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_Case_5_int(self):
        """Test Case 5: Uncle is black and the violator node is in external position."""
        self.tree.add_all([10, 5, 15, 3])
        self.tree.add(2)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_case_6_int(self):
        """Test Case 6: Uncle is black and the violator node is in internal position."""
        self.tree.add_all([10, 5, 15, 6])
        self.tree.add(7)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._RED,
                       RedBlackTree._BLACK, RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_case_1_b_remove_int(self):
        "Test Case 1b: Node to be removed is the root and have a red son"
        self.tree.add_all([10, 12])
        self.tree.remove(10)
        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._BLACK]
        self.assertEqual(tree_colors, real_colors)

    def test_Case_2_b_int(self):
        """Test Case 2: Node to be removed is red"""
        self.tree.add_all([10, 5])
        self.tree.remove(5)
        tree_color = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._BLACK]
        self.assertEqual(tree_color, real_colors)

    def test_case_5_remove_int(self):
        """
        Test Case 5: The sibling is red, and both the parent and the
        sibling's children are black.
        """
        self.tree.add_all([10, 3, 13, 16, 20, 12, 2, 5])
        self.tree.remove(3)

        tree_colors = self.tree._RedBlackTree__array_color()
        real_colors = [RedBlackTree._RED, RedBlackTree._BLACK,
                       RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._BLACK, RedBlackTree._RED,
                       RedBlackTree._BLACK]

        self.assertEqual(tree_colors, real_colors)

    def test_case_6_remove_int(self):
        """Test Case 6: The sibling is black, and both nephew are also black but the parent is red."""
        self.tree.add_all([10, 5, 17, 3, 7, 15, 25])
        self.tree._RedBlackTree__root.color = RedBlackTree._RED
        self.tree._RedBlackTree__root.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.left.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.left.right.color = RedBlackTree._BLACK
        self.tree.remove(5)
        self.assertEqual(self.tree._RedBlackTree__root.color,
                         RedBlackTree._BLACK)
        self.assertEqual(self.tree._RedBlackTree__root.right.color,
                         RedBlackTree._RED)

    def test_case_7_remove_int(self):
        """Test Case 7: The sibling is black, and furthest nephew is red."""
        self.tree.add_all([10, 5, 19, 3, 7, 15, 25])
        for node in self.tree:
            self.tree._RedBlackTree__contains(node).color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.color = RedBlackTree._RED
        self.tree._RedBlackTree__root.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.right.right.color = RedBlackTree._RED
        self.tree._RedBlackTree__root.right.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.left.left.color = RedBlackTree._BLACK
        self.tree._RedBlackTree__root.left.right.color = RedBlackTree._BLACK
        self.tree.remove(5)
        self.assertEqual(self.tree._RedBlackTree__root.color,
                         RedBlackTree._BLACK)
        self.assertEqual(self.tree._RedBlackTree__root.right.color,
                         RedBlackTree._BLACK)


if __name__ == '__main__':
    unittest.main()
