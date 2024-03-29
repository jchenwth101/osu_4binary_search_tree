from unittest import TestCase
# Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment: A4P1 bst UNIT TESTING
# Description: unit tests

import unittest
from bst import Stack, Queue, TreeNode, BST

class binarySearchTreeTests(unittest.TestCase):
    """
    definte unit tests for bst.py
    """
    def test_1(self):
        """add """
        tree = BST()
        self.assertIsNone(tree.root)
        tree.add(10)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        tree.add(15)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        tree.add(5)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        tree.add(15)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertEqual(tree.root.right.right.value, 15)
        self.assertIsNone(tree.root.right.right.left)
        self.assertIsNone(tree.root.right.right.right)
        tree.add(15)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertEqual(tree.root.right.right.value, 15)
        self.assertIsNone(tree.root.right.right.left)
        self.assertEqual(tree.root.right.right.right.value, 15)
        self.assertIsNone(tree.root.right.right.right.left)
        self.assertIsNone(tree.root.right.right.right.right)
        tree.add(5)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertEqual(tree.root.left.right.value, 5)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertEqual(tree.root.right.right.value, 15)
        self.assertIsNone(tree.root.right.right.left)
        self.assertEqual(tree.root.right.right.right.value, 15)
        self.assertIsNone(tree.root.right.right.right.left)
        self.assertIsNone(tree.root.right.right.right.right)

    def test_2(self):
        """add """
        tree = BST()
        tree.add(10)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        tree.add(10)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right.value, 10)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        tree.add(-1)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, -1)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 10)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        tree.add(5)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, -1)
        self.assertIsNone(tree.root.left.left)
        self.assertEqual(tree.root.left.right.value, 5)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 10)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        tree.add(-1)
        # print(tree)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, -1)
        self.assertIsNone(tree.root.left.left)
        self.assertEqual(tree.root.left.right.value, 5)
        self.assertEqual(tree.root.left.right.left.value, -1)
        self.assertIsNone(tree.root.left.right.left.left)
        self.assertIsNone(tree.root.left.right.left.right)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 10)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)

    def test_3(self):
        """contains """
        tree = BST([10, 5, 15])
        self.assertFalse(tree.contains(11))
        self.assertTrue(tree.contains(15))
        self.assertFalse(tree.contains(-10))
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(5))

    def test_4(self):
        """contains #2"""
        tree = BST()
        self.assertFalse(tree.contains(0))

    def test_5(self):
        """get_first"""
        tree = BST()
        self.assertIsNone(tree.get_first())
        tree.add(10)
        self.assertEqual(tree.get_first(), 10)
        tree.add(15)
        self.assertEqual(tree.get_first(), 10)
        tree.add(5)
        self.assertEqual(tree.get_first(), 10)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)

    def test_6(self):
        """remove#1"""
        tree = BST([10, 5, 15])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertFalse(tree.remove(7))
        self.assertTrue(tree.remove(15))
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertIsNone(tree.root.right)
        self.assertFalse(tree.remove(15))
        tree.add(15)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertTrue(tree.remove(5))
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.left)

    def test_7(self):
        """remove #2"""
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 20)
        self.assertIsNone(tree.root.right.right)
        self.assertEqual(tree.root.right.left.value, 15)
        self.assertEqual(tree.root.right.left.left.value, 12)
        self.assertEqual(tree.root.right.left.right.value, 17)
        self.assertIsNone(tree.root.right.left.left.left)
        self.assertIsNone(tree.root.right.left.left.right)
        self.assertIsNone(tree.root.right.left.right.left)
        self.assertIsNone(tree.root.right.left.right.right)
        self.assertTrue(tree.remove(20))
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.root.right.left.value, 12)
        self.assertEqual(tree.root.right.right.value, 17)
        self.assertIsNone(tree.root.right.left.left)
        self.assertIsNone(tree.root.right.left.right)
        self.assertIsNone(tree.root.right.right.left)
        self.assertIsNone(tree.root.right.right.right)

    def test_8(self):
        """remove#3"""
        tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.right.left.value, 18)
        self.assertEqual(tree.root.right.left.left.value, 12)
        self.assertEqual(tree.root.right.left.right.value, 18)
        self.assertIsNone(tree.root.right.left.right.left)
        self.assertIsNone(tree.root.right.left.right.right)
        self.assertIsNone(tree.root.right.left.left.left)
        self.assertIsNone(tree.root.right.left.left.right)
        self.assertEqual(tree.root.right.right.value, 27)
        self.assertEqual(tree.root.right.right.left.value, 22)
        self.assertEqual(tree.root.right.right.right.value, 30)
        self.assertIsNone(tree.root.right.right.right.left)
        self.assertIsNone(tree.root.right.right.right.right)
        self.assertEqual(tree.root.right.right.left.right.value, 24)
        self.assertIsNone(tree.root.right.right.left.right.right)
        self.assertEqual(tree.root.right.right.left.right.left.value, 22)
        self.assertIsNone(tree.root.right.right.left.right.left.left)
        self.assertIsNone(tree.root.right.right.left.right.left.right)
        self.assertTrue(tree.remove(20))
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 22)
        self.assertEqual(tree.root.right.left.value, 18)
        self.assertEqual(tree.root.right.left.left.value, 12)
        self.assertEqual(tree.root.right.left.right.value, 18)
        self.assertIsNone(tree.root.right.left.right.left)
        self.assertIsNone(tree.root.right.left.right.right)
        self.assertIsNone(tree.root.right.left.left.left)
        self.assertIsNone(tree.root.right.left.left.right)
        self.assertEqual(tree.root.right.right.value, 27)
        self.assertEqual(tree.root.right.right.left.value, 24)
        self.assertEqual(tree.root.right.right.right.value, 30)
        self.assertIsNone(tree.root.right.right.right.left)
        self.assertIsNone(tree.root.right.right.right.right)
        self.assertIsNone(tree.root.right.right.left.right)
        self.assertEqual(tree.root.right.right.left.left.value, 22)
        self.assertIsNone(tree.root.right.right.left.left.left)
        self.assertIsNone(tree.root.right.right.left.left.right)

    def test_9(self):
        """remove_first_node"""
        tree = BST([10, 15, 5])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 15)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.right)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 5)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertTrue(tree.remove_first())
        self.assertIsNone(tree.root)

    def test_10(self):
        """remove_first_node#2"""
        tree = BST([10, 20, 5, 15, 17, 7])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.right.left.value, 15)
        self.assertEqual(tree.root.right.left.right.value, 17)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.right.left.left)
        self.assertIsNone(tree.root.right.left.right.left)
        self.assertIsNone(tree.root.right.left.right.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 15)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.right.left.value, 17)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.right.left.left)
        self.assertIsNone(tree.root.right.left.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 17)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertEqual(tree.root.right.value, 20)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 20)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertIsNone(tree.root.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.right.value, 7)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.left)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 7)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertTrue(tree.remove_first())
        self.assertIsNone(tree.root)

    def test_11(self):
        """remove_first_node #3"""
        tree = BST([10, 10, -1, 5, -1])
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, -1)
        self.assertEqual(tree.root.left.right.value, 5)
        self.assertEqual(tree.root.left.right.left.value, -1)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertIsNone(tree.root.left.right.left.left)
        self.assertIsNone(tree.root.left.right.left.right)
        self.assertEqual(tree.root.right.value, 10)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, -1)
        self.assertEqual(tree.root.left.right.value, 5)
        self.assertEqual(tree.root.left.right.left.value, -1)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right.right)
        self.assertIsNone(tree.root.left.right.left.left)
        self.assertIsNone(tree.root.left.right.left.right)
        self.assertIsNone(tree.root.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, -1)
        self.assertEqual(tree.root.right.value, 5)
        self.assertEqual(tree.root.right.left.value, -1)
        self.assertIsNone(tree.root.right.right)
        self.assertIsNone(tree.root.right.left.left)
        self.assertIsNone(tree.root.right.left.right)
        self.assertIsNone(tree.root.left)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, -1)
        self.assertEqual(tree.root.right.value, 5)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right.left)
        self.assertIsNone(tree.root.right.right)
        self.assertTrue(tree.remove_first())
        self.assertEqual(tree.root.value, 5)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)
        self.assertTrue(tree.remove_first())
        self.assertIsNone(tree.root)
        self.assertFalse(tree.remove_first())

    def test_12(self):
        """Traversal methods """
        tree = BST([10, 20, 5, 15, 17, 7, 12])

        q = tree.pre_order_traversal()
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, 7)
        self.assertEqual(q.dequeue().value, 20)
        self.assertEqual(q.dequeue().value, 15)
        self.assertEqual(q.dequeue().value, 12)
        self.assertEqual(q.dequeue().value, 17)

        q = tree.in_order_traversal()
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, 7)
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 12)
        self.assertEqual(q.dequeue().value, 15)
        self.assertEqual(q.dequeue().value, 17)
        self.assertEqual(q.dequeue().value, 20)

        q = tree.post_order_traversal()
        self.assertEqual(q.dequeue().value, 7)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, 12)
        self.assertEqual(q.dequeue().value, 17)
        self.assertEqual(q.dequeue().value, 15)
        self.assertEqual(q.dequeue().value, 20)
        self.assertEqual(q.dequeue().value, 10)

        q = tree.by_level_traversal()
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, 20)
        self.assertEqual(q.dequeue().value, 7)
        self.assertEqual(q.dequeue().value, 15)
        self.assertEqual(q.dequeue().value, 12)
        self.assertEqual(q.dequeue().value, 17)

    def test_13(self):
        """Traversal methods#2"""
        tree = BST([10, 10, -1, 5, -1])
        q = tree.pre_order_traversal()
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 10)

        q = tree.in_order_traversal()
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 10)

        q = tree.post_order_traversal()
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 10)

        q = tree.by_level_traversal()
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, -1)
        self.assertEqual(q.dequeue().value, 10)
        self.assertEqual(q.dequeue().value, 5)
        self.assertEqual(q.dequeue().value, -1)

    def test_14(self):
        """is_complete #1"""
        tree = BST()
        self.assertTrue(tree.is_complete())

    def test_15(self):
        """Comprehensive example #1 """
        tree = BST()
        header = 'Value   Size  Height   Leaves   Unique   '
        header += 'Complete?  Full?    Perfect?'
        print(header)
        print('-' * len(header))
        print(f'  N/A {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')

        for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
            tree.add(value)
            print(f'{value:5} {tree.size():6} {tree.height():7} ',
                  f'{tree.count_leaves():7} {tree.count_unique():8}  ',
                  f'{str(tree.is_complete()):10}',
                  f'{str(tree.is_full()):7} ',
                  f'{str(tree.is_perfect())}')
        print()
        print(tree.pre_order_traversal())
        print(tree.in_order_traversal())
        print(tree.post_order_traversal())
        print(tree.by_level_traversal())

    def test_16(self):
        """Comprehensive"""
        tree = BST()
        header = 'Value   Size  Height   Leaves   Unique   '
        header += 'Complete?  Full?    Perfect?'
        print(header)
        print('-' * len(header))
        print(f'N/A   {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')

        for value in 'DATA STRUCTURES':
            tree.add(value)
            print(f'{value:5} {tree.size():6} {tree.height():7} ',
                  f'{tree.count_leaves():7} {tree.count_unique():8}  ',
                  f'{str(tree.is_complete()):10}',
                  f'{str(tree.is_full()):7} ',
                  f'{str(tree.is_perfect())}')
        print('', tree.pre_order_traversal(), tree.in_order_traversal(),
              tree.post_order_traversal(), tree.by_level_traversal(),
              sep='\n')

    def test_17(self):
        """count"""
        tree = BST([2, 2, 2, 2])
        self.assertEqual(1, tree.count_unique())

if __name__ == '__main__':
    unittest.main()