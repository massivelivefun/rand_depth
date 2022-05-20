from src.rand_depth.node import T, Node
from src.rand_depth.tree_operations import TreeOperations
import types
from typing import TypeVar
import unittest


class TreeOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        # left heavy tree
        l_left2 = Node("left2", None, None)
        l_left = Node("left", l_left2, None)
        l_right = Node("right", None, None)
        self.left_heavy_tree = Node("root", l_left, l_right)

        # right heavy tree
        r_right2 = Node("right2", None, None)
        r_right = Node("right", r_right2, None)
        r_left = Node("left", None, None)
        self.right_heavy_tree = Node("root", r_left, r_right)

        # single node tree
        self.root_tree = Node("root", None, None)

        # An instance of TreeOperations
        self.tree_op_class_instance = TreeOperations()

    def test_max_depth_3_bunch_of_times(self) -> None:
        num_of_trees = 9999
        max_depth = 2
        for _ in range(0, num_of_trees):
            root = TreeOperations.gen_tree(max_depth)
            self.assertEqual(TreeOperations.max_depth(root), max_depth)

    def test_max_depth_3_bunch_of_times(self) -> None:
        num_of_trees = 9999
        max_depth = 3
        for _ in range(0, num_of_trees):
            root = TreeOperations.gen_tree(max_depth)
            self.assertEqual(TreeOperations.max_depth(root), max_depth)

    def test_max_depth_4_bunch_of_times(self) -> None:
        num_of_trees = 9999
        max_depth = 4
        for _ in range(0, num_of_trees):
            root = TreeOperations.gen_tree(max_depth)
            self.assertEqual(TreeOperations.max_depth(root), max_depth)

    def test_max_depth_5_bunch_of_times(self) -> None:
        num_of_trees = 9999
        max_depth = 5
        for _ in range(0, num_of_trees):
            root = TreeOperations.gen_tree(max_depth)
            self.assertEqual(TreeOperations.max_depth(root), max_depth)

    def test_gen_tree_is_static_method(self) -> None:
        self.assertIsInstance(
            self.tree_op_class_instance.gen_tree, types.FunctionType)

    def test_max_depth_is_static_method(self) -> None:
        self.assertIsInstance(
            self.tree_op_class_instance.max_depth, types.FunctionType)

    # def test_t_is_typedef_object():
    #     assert isinstance(A, TypeVar)

    def test_t_typevar_name_is_t(self) -> None:
        self.assertEqual(T.__name__, 'T')
