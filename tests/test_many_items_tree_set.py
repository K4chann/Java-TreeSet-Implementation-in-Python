"""Module which provided a test class for TreeSet with 150 random items."""

import unittest
from model.tree_set import *
import random


class TestManyItemsTreeSet(unittest.TestCase):
    """Test TreeSet with 150 random items"""
    def setUp(self) -> None:
        """Create TreeSet with 150 random items"""
        self.items = {random.randint(0, 1000) for _ in range(150)}
        self.tree = TreeSet(int, self.items)
        self.ordered_items = sorted(list(self.items))

    def test_size_int(self):
        """Test TreeSet size"""
        self.assertEqual(self.tree.size(), len(self.items), "TreeSet must be 10")

    def test_remove_int(self):
        """Test TreeSet remove method"""
        for num in self.items:
            self.assertTrue(self.tree.remove(num), "Wrong value after deleting")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")
        self.tree.add(10)
        self.assertEqual(self.tree.size(), 1, "TreeSet size must be 1 after adding 1 item")
        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 1 item")

    def test_clear_int(self):
        """Test TreeSet clear method"""
        self.tree.clear()
        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")
        self.tree.add(10)
        self.assertEqual(self.tree.size(), 1, "TreeSet size must be 1 after adding 1 item")
        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 1 item")

    def test_higher_int(self):
        """Test TreeSet higher method"""
        for index, item in enumerate(self.ordered_items[:-1]):
            self.assertEqual(self.tree.higher(item), self.ordered_items[index + 1], "Wrong higher value")

    def test_lower_int(self):
        """Test TreeSet lower method"""
        for index, item in enumerate(self.ordered_items[1:]):
            self.assertEqual(self.tree.lower(item), self.ordered_items[index], "Wrong lower value")

    def test_ceiling_int(self):
        """Test TreeSet ceiling method"""
        for index, item in enumerate(self.ordered_items):
            self.assertEqual(self.tree.ceiling(item), self.ordered_items[index], "Wrong ceiling value")

    def test_floor_int(self):
        """Test TreeSet floor method"""
        for index, item in enumerate(self.ordered_items):
            self.assertEqual(self.tree.floor(item), self.ordered_items[index], "Wrong ceiling value")

    def test_first_int(self):
        """Test TreeSet first method"""
        self.assertEqual(self.tree.first(), min(self.items), "Wrong TreeSet first value")
        self.tree.add(-1)
        self.assertEqual(self.tree.first(), -1, "Wrong TreeSet first value")
        self.assertEqual(self.tree.size(), len(self.items) + 1, "Wrong TreeSet size")

    def test_last_int(self):
        """Test TreeSet last method"""
        self.assertEqual(self.tree.last(), max(self.items), "Wrong TreeSet last value")
        self.tree.add(1001)
        self.assertEqual(self.tree.last(), 1001, "Wrong TreeSet last value")
        self.assertEqual(self.tree.size(), len(self.items) + 1, "Wrong TreeSet size")

    def test_poll_first_int(self):
        """Test TreeSet poll_first method"""
        items_len = self.tree.size()

        for index in range(items_len):
            self.assertEqual(self.tree.poll_first(), self.ordered_items[index],
                             "Wrong deleted first value from TreeSet")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")

    def test_poll_last_int(self):
        """Test TreeSet poll_last method"""
        items_len = self.tree.size()

        for index in range(items_len - 1, -1, -1):
            self.assertEqual(
                self.tree.poll_last(), self.ordered_items[index], "Wrong deleted last value from TreeSet"
            )

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")

    def test_iterator_int(self):
        """Test TreeSet iteration"""
        for index, item in enumerate(self.tree.iterator()):
            self.assertEqual(item, self.ordered_items[index], "Wrong value when using TreeSet iteration")

    def test_descending_iterator_int(self):
        """Test TreeSet descending iteration"""
        for index, item in enumerate(self.tree.descending_iterator()):
            self.assertEqual(
                item, self.ordered_items[len(self.ordered_items) - 1 - index],
                "Wrong value when using TreeSet descending iterator"
            )

    def test_clone_int(self):
        """Test TreeSet clone method"""
        cloned_tree = self.tree.clone()
        self.assertEqual(self.tree, cloned_tree, "Cloned tree is not equal to base tree")
        self.assertEqual(self.tree.size(), cloned_tree.size())
        self.assertFalse(cloned_tree.is_empty())


if __name__ == '__main__':
    unittest.main()
