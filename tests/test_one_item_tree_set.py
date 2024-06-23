"""Module which provides a test class for TreeSet with one item."""

import unittest
from model.tree_set import *


class TestOneItemTreeSet(unittest.TestCase):
    """Test class for TreeSet with one item."""

    def setUp(self):
        """Set up TreeSet with one item."""
        self.tree_int = TreeSet(int, [10])
        self.tree_str = TreeSet(str, ["9"])
        self.tree_float = TreeSet(float, [10.0])
        self.tree_person = TreeSet(Person, [Person("John", 20)])

    def test_size_int(self):
        """Test size method for TreeSet with int type."""
        self.assertEqual(self.tree_int.size(), 1, "Size of tree is not 1")

    def test_is_empty_int(self):
        """Test is_empty method for TreeSet with int type."""
        self.assertFalse(self.tree_int.is_empty(), "Tree is empty")

    def test_clone_int(self):
        """Test clone method for TreeSet with int type."""
        clone = self.tree_int.clone()
        self.assertEqual(clone.size(), 1, "Clone size is not 1")
        self.assertEqual(clone, self.tree_int, "Clone is not equal to tree")
        self.assertFalse(clone.is_empty(), "Clone is empty")
        self.assertEqual(clone.first(), 10, "First element is not 10")
        self.assertEqual(clone.last(), 10, "Last element is not 10")
        self.assertEqual(
            list(clone.iterator()),
            list(self.tree_int.iterator()),
            "Iterators are not equal"
        )
        self.assertEqual(
            list(clone.descending_iterator()),
            list(self.tree_int.descending_iterator()),
            "Descending iterators are not equal"
        )

    def test_first_int(self):
        """Test first method for TreeSet with int type."""
        self.assertEqual(self.tree_int.first(), 10, "First element is not 10")
        self.tree_int.add(5)
        self.assertEqual(self.tree_int.first(), 5, "First element is not 5")
        self.tree_int.add(15)
        self.assertEqual(self.tree_int.first(), 5, "First element is not 5")
        self.assertEqual(self.tree_int.size(), 3, "Size of tree is not 3")

    def test_last_int(self):
        """Test last method for TreeSet with int type."""
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")
        self.tree_int.add(5)
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")
        self.tree_int.add(15)
        self.assertEqual(self.tree_int.last(), 15, "Last element is not 15")
        self.assertEqual(self.tree_int.size(), 3, "Size of tree is not 3")

    def test_iterator_int(self):
        """Test iterator method for TreeSet with int type."""
        self.assertEqual(
            next(self.tree_int.iterator()), 10,
            "Iterator element is not 10"
        )
        self.tree_int.add(5)
        self.assertEqual(
            next(self.tree_int.iterator()), 5,
            "Iterator element is not 5"
        )
        self.tree_int.add(15)
        self.assertEqual(
            [5, 10, 15], list(self.tree_int),
            "Iterator elements are not [5, 10, 15"
        )

    def test_descending_iterator_int(self):
        """Test descending_iterator method for TreeSet with int type."""
        self.assertEqual(next(self.tree_int.descending_iterator()), 10, "Descending iterator element is not 10")
        self.tree_int.add(5)
        self.assertEqual(next(self.tree_int.descending_iterator()), 10, "Descending iterator element is not 10")
        self.tree_int.add(15)
        self.assertEqual(
            [15, 10, 5], list(self.tree_int.descending_iterator()),
            "Descending iterator elements are not [15, 10, 5]"
        )

    def test1_add_int(self):
        """Test add method for TreeSet with int type."""
        self.tree_int.add(5)
        self.assertEqual(self.tree_int.size(), 2, "Size of tree is not 2")
        self.assertEqual(self.tree_int.first(), 5, "First element is not 5")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")
        self.assertTrue(self.tree_int.contains(5), "Tree does not contain 5")
        self.assertFalse(self.tree_int.is_empty(), "Tree is empty")
        self.assertFalse(self.tree_int.add(5), "Element 5 is already added")
        self.assertFalse(self.tree_int.add(10), "Element 10 is already added")
        self.assertEqual(self.tree_int.size(), 2, "Size of tree is not 2")

    def test2_add_int(self):
        """Test add method for TreeSet with int type."""
        with self.assertRaises(TypeError):
            self.tree_int.add("10")

    def test1_add_all_int(self):
        """Test add_all method for TreeSet with int type."""
        self.assertTrue(
            self.tree_int.add_all([num for num in range(10)]),
            "Elements are not added"
        )
        self.assertEqual(self.tree_int.size(), 11, "Size of tree is not 10")
        self.assertEqual(self.tree_int.first(), 0, "First element is not 0")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")
        self.assertFalse(self.tree_int.is_empty(), "Tree is empty")
        self.assertFalse(
            self.tree_int.add_all([num for num in range(10)]),
            "Elements are already added"
        )
        self.assertEqual(self.tree_int.size(), 11, "Size of tree is not 10")
        self.assertEqual(self.tree_int.first(), 0, "First element is not 0")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test2_add_all_int(self):
        """Test add_all method for TreeSet with int type."""
        with self.assertRaises(TypeError):
            self.tree_int.add_all([str(num) for num in range(10)])

        self.assertEqual(self.tree_int.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_int.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test3_add_all_int(self):
        """Test add_all method for TreeSet with int type."""
        with self.assertRaises(TypeError):
            self.tree_int.add_all(
                [str(num) if num % 2 == 0 else num for num in range(10)]
            )

        self.assertEqual(self.tree_int.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_int.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test_add_none_int(self):
        """Test add method for TreeSet with int type."""
        with self.assertRaises(NullPointerException):
            self.tree_int.add(None)

    def test_add_all_none_int(self):
        """Test add_all method for TreeSet with int type."""
        with self.assertRaises(NullPointerException):
            self.tree_int.add_all([None])

    def test1_remove_int(self):
        """Test remove method for TreeSet with int type."""
        self.assertTrue(self.tree_int.remove(10), "Element is not removed")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_int.is_empty(), "Tree is not empty")
        self.assertFalse(self.tree_int.remove(10), "Element is already removed")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")

    def test2_remove_int(self):
        """Test remove method for TreeSet with int type."""
        with self.assertRaises(NullPointerException):
            self.tree_int.remove(None)

    def test3_remove_int(self):
        """Test remove method for TreeSet with int type."""
        with self.assertRaises(TypeError):
            self.tree_int.remove("10")

        self.assertEqual(self.tree_int.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_int.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test1_contains_int(self):
        """Test contains method for TreeSet with int type."""
        self.assertFalse(self.tree_int.contains(15), "Tree contains 15")
        self.assertTrue(self.tree_int.contains(10), "Tree does not contain 10")
        self.assertFalse(self.tree_int.contains(5), "Tree contains 5")

    def test2_contains_int(self):
        """Test contains method for TreeSet with int type."""
        with self.assertRaises(NullPointerException):
            self.tree_int.contains(None)

    def test_poll_first_int(self):
        """Test poll_first method for TreeSet with int type."""
        self.assertEqual(self.tree_int.poll_first(), 10, "First element is not 10")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_int.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_int.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_int.descending_iterator()), "Tree is not empty")

    def test_poll_last_int(self):
        """Test poll_last method for TreeSet with int type."""
        self.assertEqual(self.tree_int.poll_last(), 10, "Last element is not 10")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_int.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_int.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_int.descending_iterator()), "Tree is not empty")

    def test_floor_int(self):
        """Test floor method for TreeSet with int type."""
        self.assertEqual(self.tree_int.floor(15), 10, "Floor element is not 10")
        self.assertEqual(self.tree_int.floor(10), 10, "Floor element is not 10")
        self.assertIsNone(self.tree_int.floor(5), "Floor element is not None")

    def test_ceiling_int(self):
        """Test ceiling method for TreeSet with int type."""
        """Test ceiling method for TreeSet with int type."""
        self.assertEqual(self.tree_int.ceiling(5), 10, "Ceiling element is not 5")
        self.assertEqual(self.tree_int.ceiling(10), 10, "Ceiling element is not 10")
        self.assertIsNone(self.tree_int.ceiling(15), "Ceiling element is not None")

    def test_higher_int(self):
        """Test higher method for TreeSet with int type."""
        self.assertEqual(self.tree_int.higher(5), 10, "Higher element is not 10")
        self.assertIsNone(self.tree_int.higher(10), "Higher element is not None")
        self.assertIsNone(self.tree_int.higher(15), "Higher element is not None")

    def test_lower_int(self):
        """Test lower method for TreeSet with int type."""
        self.assertEqual(self.tree_int.lower(15), 10, "Lower element is not 10")
        self.assertIsNone(self.tree_int.lower(10), "Lower element is not None")
        self.assertIsNone(self.tree_int.lower(5), "Lower element is not None")

    def test_size_str(self):
        """Test size method for TreeSet with str type."""
        self.assertEqual(self.tree_str.size(), 1, "Size of tree is not 1")

    def test_is_empty_str(self):
        """Test is_empty method for TreeSet with str type."""
        self.assertFalse(self.tree_str.is_empty(), "Tree is empty")

    def test_clone_str(self):
        """Test clone method for TreeSet with str type."""
        clone = self.tree_str.clone()
        self.assertEqual(clone.size(), 1, "Clone size is not 1")
        self.assertEqual(clone, self.tree_str, "Clone is not equal to tree")
        self.assertFalse(clone.is_empty(), "Clone is empty")
        self.assertEqual(clone.first(), "9", "First element is not 10")
        self.assertEqual(clone.last(), "9", "Last element is not 10")
        self.assertEqual(
            list(clone.iterator()),
            list(self.tree_str.iterator()),
            "Iterators are not equal"
        )
        self.assertEqual(
            list(clone.descending_iterator()),
            list(self.tree_str.descending_iterator()),
            "Descending iterators are not equal"
        )

    def test_first_str(self):
        """Test first method for TreeSet with str type."""
        self.assertEqual(self.tree_str.first(), "9", "First element is not 10")
        self.tree_str.add("5")
        self.assertEqual(self.tree_str.first(), "5", "First element is not 5")
        self.tree_str.add("99")
        self.assertEqual(self.tree_str.first(), "5", "First element is not 5")
        self.assertEqual(self.tree_str.size(), 3, "Size of tree is not 3")

    def test_last_str(self):
        """Test last method for TreeSet with str type."""
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 10")
        self.tree_str.add("5")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 10")
        self.tree_str.add("99")
        self.assertEqual(self.tree_str.last(), "99", "Last element is not 99")
        self.assertEqual(self.tree_str.size(), 3, "Size of tree is not 3")

    def test_iterator_str(self):
        """Test iterator method for TreeSet with str type."""
        self.assertEqual(
            next(self.tree_str.iterator()), "9",
            "Iterator element is not 9"
        )
        self.tree_str.add("5")
        self.assertEqual(
            next(self.tree_str.iterator()), "5",
            "Iterator element is not 5"
        )
        self.tree_str.add("99")
        self.assertEqual(
            ["5", "9", "99"], list(self.tree_str),
            "Iterator elements are not [5, 9, 99]"
        )

    def test_descending_iterator_str(self):
        """Test descending_iterator method for TreeSet with str type."""
        self.assertEqual(next(self.tree_str.descending_iterator()), "9", "Descending iterator element is not 9")
        self.tree_str.add("5")
        self.assertEqual(next(self.tree_str.descending_iterator()), "9", "Descending iterator element is not 9")
        self.tree_str.add("99")
        self.assertEqual(
            ["99", "9", "5"], list(self.tree_str.descending_iterator()),
            "Descending iterator elements are not [99, 10, 5]"
        )

    def test1_add_str(self):
        """Test add method for TreeSet with str type."""
        self.tree_str.add("5")
        self.assertEqual(self.tree_str.size(), 2, "Size of tree is not 2")
        self.assertEqual(self.tree_str.first(), "5", "First element is not 5")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")
        self.assertTrue(self.tree_str.contains("5"), "Tree does not contain 5")
        self.assertFalse(self.tree_str.is_empty(), "Tree is empty")
        self.assertFalse(self.tree_str.add("5"), "Element 5 is already added")
        self.assertFalse(self.tree_str.add("9"), "Element 9 is already added")
        self.assertEqual(self.tree_str.size(), 2, "Size of tree is not 2")

    def test2_add_str(self):
        """Test add method for TreeSet with str type."""
        with self.assertRaises(TypeError):
            self.tree_str.add(10)

    def test1_add_all_str(self):
        """Test add_all method for TreeSet with str type."""
        self.assertTrue(
            self.tree_str.add_all([str(num) for num in range(9)]),
            "Elements are not added"
        )
        self.assertEqual(self.tree_str.size(), 10, "Size of tree is not 10")
        self.assertEqual(self.tree_str.first(), "0", "First element is not 0")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")
        self.assertFalse(self.tree_str.is_empty(), "Tree is empty")
        self.assertFalse(
            self.tree_str.add_all([str(num) for num in range(9)]),
            "Elements are already added"
        )
        self.assertEqual(self.tree_str.size(), 10, "Size of tree is not 10")
        self.assertEqual(self.tree_str.first(), "0", "First element is not 0")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")

    def test2_add_all_str(self):
        """Test add_all method for TreeSet with str type."""
        with self.assertRaises(TypeError):
            self.tree_str.add_all([num for num in range(9)])

        self.assertEqual(self.tree_str.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_str.first(), "9", "First element is not 9")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")

    def test3_add_all_str(self):
        """Test add_all method for TreeSet with str type."""
        with self.assertRaises(TypeError):
            self.tree_str.add_all(
                [str(num) if num % 2 == 0 else num for num in range(10)]
            )

        self.assertEqual(self.tree_str.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_str.first(), "9", "First element is not 9")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")

    def test_add_none_str(self):
        """Test add method for TreeSet with str type."""
        with self.assertRaises(NullPointerException):
            self.tree_str.add(None)

    def test_add_all_none_str(self):
        """Test add_all method for TreeSet with str type."""
        with self.assertRaises(NullPointerException):
            self.tree_str.add_all([None])

    def test1_remove_str(self):
        """Test remove method for TreeSet with str type."""
        self.assertTrue(self.tree_str.remove("9"), "Element is not removed")
        self.assertEqual(self.tree_str.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_str.is_empty(), "Tree is not empty")
        self.assertFalse(self.tree_str.remove("9"), "Element is already removed")
        self.assertEqual(self.tree_str.size(), 0, "Size of tree is not 0")

    def test2_remove_str(self):
        """Test remove method for TreeSet with str type."""
        with self.assertRaises(NullPointerException):
            self.tree_str.remove(None)

    def test3_remove_str(self):
        """Test remove method for TreeSet with str type."""
        with self.assertRaises(TypeError):
            self.tree_str.remove(9)

        self.assertEqual(self.tree_str.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_str.first(), "9", "First element is not 9")
        self.assertEqual(self.tree_str.last(), "9", "Last element is not 9")

    def test1_contains_str(self):
        """Test contains method for TreeSet with str type."""
        self.assertFalse(self.tree_str.contains("99"), "Tree contains 99")
        self.assertTrue(self.tree_str.contains("9"), "Tree does not contain 9")
        self.assertFalse(self.tree_str.contains("5"), "Tree contains 5")

    def test2_contains_str(self):
        """Test contains method for TreeSet with str type."""
        with self.assertRaises(NullPointerException):
            self.tree_str.contains(None)

    def test_poll_first_str(self):
        """Test poll_first method for TreeSet with str type."""
        self.assertEqual(self.tree_str.poll_first(), "9", "First element is not 9")
        self.assertEqual(self.tree_str.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_str.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_str.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_str.descending_iterator()), "Tree is not empty")

    def test_poll_last_str(self):
        """Test poll_last method for TreeSet with str type."""
        self.assertEqual(self.tree_str.poll_last(), "9", "Last element is not 9")
        self.assertEqual(self.tree_str.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_str.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_str.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_str.descending_iterator()), "Tree is not empty")

    def test_floor_str(self):
        """Test floor method for TreeSet with str type."""
        self.assertEqual(self.tree_str.floor("99"), "9", "Floor element is not 9")
        self.assertEqual(self.tree_str.floor("9"), "9", "Floor element is not 9")
        self.assertIsNone(self.tree_str.floor("5"), "Floor element is not None")

    def test_ceiling_str(self):
        """Test ceiling method for TreeSet with str type."""
        """Test ceiling method for TreeSet with str type."""
        self.assertEqual(self.tree_str.ceiling("5"), "9", "Ceiling element is not 5")
        self.assertEqual(self.tree_str.ceiling("9"), "9", "Ceiling element is not 10")
        self.assertIsNone(self.tree_str.ceiling("99"), "Ceiling element is not None")

    def test_higher_str(self):
        """Test higher method for TreeSet with str type."""
        self.assertEqual(self.tree_str.higher("5"), "9", "Higher element is not 9")
        self.assertIsNone(self.tree_str.higher("9"), "Higher element is not None")
        self.assertIsNone(self.tree_str.higher("99"), "Higher element is not None")

    def test_lower_str(self):
        """Test lower method for TreeSet with str type."""
        self.assertEqual(self.tree_str.lower("99"), "9", "Lower element is not 9")
        self.assertIsNone(self.tree_str.lower("9"), "Lower element is not None")
        self.assertIsNone(self.tree_str.lower("5"), "Lower element is not None")

    def test_size_float(self):
        """Test size method for TreeSet with float type."""
        self.assertEqual(self.tree_float.size(), 1, "Size of tree is not 1")

    def test_is_empty_float(self):
        """Test is_empty method for TreeSet with float type."""
        self.assertFalse(self.tree_float.is_empty(), "Tree is empty")

    def test_clone_float(self):
        """Test clone method for TreeSet with float type."""
        clone = self.tree_float.clone()
        self.assertEqual(clone.size(), 1, "Clone size is not 1")
        self.assertEqual(clone, self.tree_float, "Clone is not equal to tree")
        self.assertFalse(clone.is_empty(), "Clone is empty")
        self.assertEqual(clone.first(), 10, "First element is not 10")
        self.assertEqual(clone.last(), 10, "Last element is not 10")
        self.assertEqual(
            list(clone.iterator()),
            list(self.tree_float.iterator()),
            "Iterators are not equal"
        )
        self.assertEqual(
            list(clone.descending_iterator()),
            list(self.tree_float.descending_iterator()),
            "Descending iterators are not equal"
        )

    def test_first_float(self):
        """Test first method for TreeSet with float type."""
        self.assertEqual(self.tree_float.first(), 10, "First element is not 10")
        self.tree_float.add(5.0)
        self.assertEqual(self.tree_float.first(), 5, "First element is not 5")
        self.tree_float.add(15.0)
        self.assertEqual(self.tree_float.first(), 5, "First element is not 5")
        self.assertEqual(self.tree_float.size(), 3, "Size of tree is not 3")

    def test_last_float(self):
        """Test last method for TreeSet with float type."""
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")
        self.tree_float.add(5.0)
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")
        self.tree_float.add(15.0)
        self.assertEqual(self.tree_float.last(), 15, "Last element is not 15")
        self.assertEqual(self.tree_float.size(), 3, "Size of tree is not 3")

    def test_iterator_float(self):
        """Test iterator method for TreeSet with float type."""
        self.assertEqual(
            next(self.tree_float.iterator()), 10,
            "Iterator element is not 10"
        )
        self.tree_float.add(5.0)
        self.assertEqual(
            next(self.tree_float.iterator()), 5,
            "Iterator element is not 5"
        )
        self.tree_float.add(15.0)
        self.assertEqual(
            [5, 10, 15], list(self.tree_float),
            "Iterator elements are not [5, 10, 15"
        )

    def test_descending_iterator_float(self):
        """Test descending_iterator method for TreeSet with float type."""
        self.assertEqual(next(self.tree_float.descending_iterator()), 10, "Descending iterator element is not 10")
        self.tree_float.add(5.0)
        self.assertEqual(next(self.tree_float.descending_iterator()), 10, "Descending iterator element is not 10")
        self.tree_float.add(15.0)
        self.assertEqual(
            [15, 10, 5], list(self.tree_float.descending_iterator()),
            "Descending iterator elements are not [15, 10, 5]"
        )

    def test1_add_float(self):
        """Test add method for TreeSet with float type."""
        self.tree_float.add(5.0)
        self.assertEqual(self.tree_float.size(), 2, "Size of tree is not 2")
        self.assertEqual(self.tree_float.first(), 5, "First element is not 5")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")
        self.assertTrue(self.tree_float.contains(5.0), "Tree does not contain 5")
        self.assertFalse(self.tree_float.is_empty(), "Tree is empty")
        self.assertFalse(self.tree_float.add(5.0), "Element 5 is already added")
        self.assertFalse(self.tree_float.add(10.0), "Element 10 is already added")
        self.assertEqual(self.tree_float.size(), 2, "Size of tree is not 2")

    def test2_add_float(self):
        """Test add method for TreeSet with float type."""
        with self.assertRaises(TypeError):
            self.tree_float.add("10")

    def test1_add_all_float(self):
        """Test add_all method for TreeSet with float type."""
        self.assertTrue(
            self.tree_float.add_all([float(num) for num in range(10)]),
            "Elements are not added"
        )
        self.assertEqual(self.tree_float.size(), 11, "Size of tree is not 10")
        self.assertEqual(self.tree_float.first(), 0, "First element is not 0")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")
        self.assertFalse(self.tree_float.is_empty(), "Tree is empty")
        self.assertFalse(
            self.tree_float.add_all([float(num) for num in range(10)]),
            "Elements are already added"
        )
        self.assertEqual(self.tree_float.size(), 11, "Size of tree is not 10")
        self.assertEqual(self.tree_float.first(), 0, "First element is not 0")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")

    def test2_add_all_float(self):
        """Test add_all method for TreeSet with float type."""
        with self.assertRaises(TypeError):
            self.tree_float.add_all([str(num) for num in range(10)])

        self.assertEqual(self.tree_float.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_float.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")

    def test3_add_all_float(self):
        """Test add_all method for TreeSet with float type."""
        with self.assertRaises(TypeError):
            self.tree_float.add_all(
                [str(num) if num % 2 == 0 else float(num) for num in range(10)]
            )

        self.assertEqual(self.tree_float.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_float.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")

    def test_add_none_float(self):
        """Test add method for TreeSet with float type."""
        with self.assertRaises(NullPointerException):
            self.tree_float.add(None)

    def test_add_all_none_float(self):
        """Test add_all method for TreeSet with float type."""
        with self.assertRaises(NullPointerException):
            self.tree_float.add_all([None])

    def test1_remove_float(self):
        """Test remove method for TreeSet with float type."""
        self.assertTrue(self.tree_float.remove(10.0), "Element is not removed")
        self.assertEqual(self.tree_float.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_float.is_empty(), "Tree is not empty")
        self.assertFalse(self.tree_float.remove(10.0), "Element is already removed")
        self.assertEqual(self.tree_float.size(), 0, "Size of tree is not 0")

    def test2_remove_float(self):
        """Test remove method for TreeSet with float type."""
        with self.assertRaises(NullPointerException):
            self.tree_float.remove(None)

    def test3_remove_float(self):
        """Test remove method for TreeSet with float type."""
        with self.assertRaises(TypeError):
            self.tree_float.remove("10")

        self.assertEqual(self.tree_float.size(), 1, "Size of tree is not 1")
        self.assertEqual(self.tree_float.first(), 10, "First element is not 10")
        self.assertEqual(self.tree_float.last(), 10, "Last element is not 10")

    def test1_contains_float(self):
        """Test contains method for TreeSet with float type."""
        self.assertFalse(self.tree_float.contains(15.0), "Tree contains 15")
        self.assertTrue(self.tree_float.contains(10.0), "Tree does not contain 10")
        self.assertFalse(self.tree_float.contains(5.0), "Tree contains 5")

    def test2_contains_float(self):
        """Test contains method for TreeSet with float type."""
        with self.assertRaises(NullPointerException):
            self.tree_float.contains(None)

    def test_poll_first_float(self):
        """Test poll_first method for TreeSet with float type."""
        self.assertEqual(self.tree_float.poll_first(), 10, "First element is not 10")
        self.assertEqual(self.tree_float.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_float.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_float.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_float.descending_iterator()), "Tree is not empty")

    def test_poll_last_float(self):
        """Test poll_last method for TreeSet with float type."""
        self.assertEqual(self.tree_float.poll_last(), 10, "Last element is not 10")
        self.assertEqual(self.tree_float.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_float.is_empty(), "Tree is not empty")
        self.assertEqual([], list(self.tree_float.iterator()), "Tree is not empty")
        self.assertEqual([], list(self.tree_float.descending_iterator()), "Tree is not empty")

    def test_floor_float(self):
        """Test floor method for TreeSet with float type."""
        self.assertEqual(self.tree_float.floor(15.0), 10, "Floor element is not 10")
        self.assertEqual(self.tree_float.floor(10.0), 10, "Floor element is not 10")
        self.assertIsNone(self.tree_float.floor(5.0), "Floor element is not None")

    def test_ceiling_float(self):
        """Test ceiling method for TreeSet with float type."""
        """Test ceiling method for TreeSet with float type."""
        self.assertEqual(self.tree_float.ceiling(5.0), 10, "Ceiling element is not 5")
        self.assertEqual(self.tree_float.ceiling(10.0), 10, "Ceiling element is not 10")
        self.assertIsNone(self.tree_float.ceiling(15.0), "Ceiling element is not None")

    def test_higher_float(self):
        """Test higher method for TreeSet with float type."""
        self.assertEqual(self.tree_float.higher(5.0), 10, "Higher element is not 10")
        self.assertIsNone(self.tree_float.higher(10.0), "Higher element is not None")
        self.assertIsNone(self.tree_float.higher(15.0), "Higher element is not None")

    def test_lower_float(self):
        """Test lower method for TreeSet with float type."""
        self.assertEqual(self.tree_float.lower(15.0), 10, "Lower element is not 10")
        self.assertIsNone(self.tree_float.lower(10.0), "Lower element is not None")
        self.assertIsNone(self.tree_float.lower(5.0), "Lower element is not None")


if __name__ == '__main__':
    unittest.main()