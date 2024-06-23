"""Main module to run the tests."""

import unittest
from model.tree_gui import GUI


def suite():
    """Create a test suite with all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_one_item_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_other_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_simple_stack"))
    suite.addTest(loader.loadTestsFromName("tests.test_tree_set_rotations_recolors"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

    # Uncomment the next lines and execute the program to see the GUI
    app = GUI()
    app.mainloop()
