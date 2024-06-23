"""
data_utils module.

This module provides three different minor data structures classes.
    1. SimpleStack
    2. Node
    3. TreeNode
"""

from enum import Enum
from typing import *


class SimpleStack:
    """
    Class that represents a stack.
    """

    def __init__(self, value: Any = None) -> None:
        """
        Constructor of the class.
        Initializes a new instance of SimpleStack.

        :param value: the initial value to push onto the stack, default is None
        :type value: Any
        """
        self.__items = list()
        self.__index = -1
        self.__next_index = -1

        if value:
            if isinstance(value, Collection):
                for item in value:
                    self.push(item)
            else:
                self.push(value)

    def push(self, value: Any) -> None:
        """
        Pushes a new value onto the stack.

        :param value: the value to push
        :type value: Any
        """
        self.__items.append(value)
        self.__index += 1
        self.__next_index = self.__index

    def pull(self) -> Any:
        """
        Pulls a value from the stack.

        :return: the pulled value.
        :rtype: Any
        :raises IndexError: if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is already empty")

        self.__index -= 1
        self.__next_index = self.__index
        return self.__items.pop()

    def peek(self) -> Any:
        """
        Returns the value at the top of the stack without removing it.

        :return: the value at the top of the stack
        :rtype: Any
        :raises IndexError: if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.__items[self.__index]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise
        :rtype: bool
        """
        return len(self.__items) == 0

    def __len__(self) -> int:
        """
        Returns the length of the stack.

        :return: the length of the stack
        :rtype: int
        """
        return len(self.__items)

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for the stack.

        :return: an iterator for the stack
        :rtype: Iterator[Any]
        """
        return self

    def __next__(self) -> Any:
        """
        Returns the next value from the stack iterator.

        :return: the next value from the stack iterator
        :rtype: Any
        :raises StopIteration: if there are no more items to return
        """
        if self.__next_index < 0:
            self.__next_index = len(self.__items) - 1
            raise StopIteration
        item = self.__items[self.__next_index]
        self.__next_index -= 1
        return item

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        :return: a string representation of the stack
        :rtype: str
        """
        return repr(self)

    def __repr__(self):
        """
        Returns a string representation of the stack for debugging.

        :return: a string representation of the stack
        :rtype: str
        """
        return f"SimpleStack({[item for item in self]})"


class Node:
    """
    Class that represents a node in a data structure (like a linked list or a tree).
    Each node has a value and pointers to the next and previous nodes.
    """

    def __init__(self, value: Any) -> None:
        """
        Constructor of the class.
        Initializes a new instance of Node.

        :param value: the initial value of the node
        :type value: Any
        """
        self.value = value
        self.next_node = None
        self.previous_node = None

    @property
    def value(self) -> Any:
        """
        Getter for the value of the node.

        :return: the value of the node
        :rtype: Any
        """
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Setter for the value of the node.
        :param value: the new value for the node
        :type value: Any
        """
        self.__value = value

    @property
    def next_node(self) -> Any:
        """
        Getter for the next node.

        :return: the next node
        :rtype: Any
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: Any) -> None:
        """
        Setter for the next node.

        :param next_node: the new next node
        :type next_node: Any
        """
        self.__next_node = next_node

    @property
    def previous_node(self) -> Any:
        """
        Getter for the previous node.

        :return: the previous node
        :rtype: Any
        """
        return self.__previous_node

    @previous_node.setter
    def previous_node(self, previous_node: Any) -> None:
        """
        Setter for the previous node.

        :param previous_node: the new previous node
        :type previous_node: Any
        """
        self.__previous_node = previous_node

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        :return: a string representation of the node
        :rtype: str
        """
        return repr(self)

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.

        :return: a string representation of the node
        :rtype: str
        """
        return f"Node({self.value})"

    def __eq__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is equal to the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the nodes are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, TreeNode):
            return self.value == other.value
        return False

    def __lt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is less than the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the current node is less than the other node, False otherwise
        :rtype: bool
        """
        if isinstance(other, TreeNode):
            return self.value < other.value
        return False

    def __gt__(self, other: 'TreeNode') -> bool:
        """
        Checks if the current node is greater than the other node.

        :param other: the other node to compare with
        :type other: TreeNode
        :return: True if the current node is greater than the other node, False otherwise
        :rtype: bool
        """
        if isinstance(other, TreeNode):
            return not self < other
        return False


class TreeNode(Node):
    """
    Class that represents a TreeNode, which is a specialized Node that also
    includes a color property. This class is used in the RedBlackTree data
    structure.
    """

    class TreeNodeUtils(Enum):
        """
        Enum class that represents the possible colors of a TreeNode in a
        RedBlackTree.
        """
        RED = 1
        BLACK = 0
        NULL = -1

    def __init__(
            self, value: Any, left: Union['TreeNode', None],
            right: Union['TreeNode', None],
            color: 'TreeNode.TreeNodeUtils' = TreeNodeUtils.RED
    ) -> None:
        """
        Constructor of the class.
        Initializes a new instance of TreeNode.

        :param value: the initial value of the node
        :type value: Any
        :param left: the left child of the node, default is None
        :type left: Union['TreeNode', None]
        :param right: the right child of the node, default is None
        :type right: Union['TreeNode', None]
        :param color: the color of the node, default is RED
        :type color: 'TreeNode.TreeNodeUtils'
        """
        super().__init__(value)
        self.parent = None
        self.color = color
        self.left = left
        self.right = right

    @property
    def color(self) -> TreeNodeUtils:
        """
        Getter for the color of the node.

        :return: the color of the node
        :rtype: TreeNode.TreeNodeUtils
        """
        return self.__color

    @color.setter
    def color(self, color: TreeNodeUtils) -> None:
        """
        Setter for the color of the node.

        :param color: the new color for the node
        :type color: TreeNode.TreeNodeUtils
        """
        assert isinstance(color,
                          TreeNode.TreeNodeUtils), "Value type should be Color"
        assert color in {TreeNode.TreeNodeUtils.RED,
                         TreeNode.TreeNodeUtils.BLACK}, \
            "Value must be 0 ('BLACK') or 1 ('RED')"

        self.__color = color

    @property
    def left(self) -> Any:
        """
        Getter for the left child of the node.

        :return: the left child of the node
        :rtype: Any
        """
        return self.__left

    @left.setter
    def left(self, node: 'TreeNode') -> None:
        """
        Setter for the left child of the node.

        :param node: the new left child for the node
        :type node: 'TreeNode'
        """
        self.__left = node

    @property
    def right(self) -> Any:
        """
        Getter for the right child of the node.

        :return: the right child of the node
        :rtype: Any
        """
        return self.__right

    @right.setter
    def right(self, node: 'TreeNode') -> None:
        """
        Setter for the right child of the node.

        :param node: the new right child for the node
        :type node: 'TreeNode'
        """
        self.__right = node

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        :return: a string representation of the node
        :rtype: str
        """
        return repr(self)

    def __repr__(self) -> str:
        """
        Returns a string representation of the node for debugging.

        :return: a string representation of the node
        :rtype: str
        """
        return f"TreeNode({self.value}, {self.left}, {self.right}, {self.color})"


if __name__ == "__main__":
    stack = SimpleStack()

    for num in range(10):
        stack.push(num)

    print(stack)

    node = Node(10)
    print(node)

    tree_node = TreeNode(10, None, None)
    print(tree_node)
