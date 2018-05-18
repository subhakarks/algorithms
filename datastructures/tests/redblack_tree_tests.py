#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : redblack_tree_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for Red-Black Tree implementation
#
# ---------------------------------------------------------------------
import unittest
from algorithms.redblack_tree import rb_tree
from algorithms.tests.common import (generate_random_list,
                                     get_rbt_from_list,
                                     get_bst_from_list)

data_one = [9]
data_left = [9, 6, 3]
data_right = [3, 6, 9]
data_center = [6, 3, 9]
ascend = [3, 6, 9]
descend = [9, 6, 3]
test_list = [81, 54, 90, 36, 69, 136, 45, 63, 89, 96]
test_list2 = [81, 54, 90, 136, 89, 94, 69, 36, 45, 63, 65, 61]


class rb_tree_unit_tests(unittest.TestCase):
    def test_rbt_init(self):
        rbt = rb_tree()
        self.assertEqual(rbt.bst_get_size_r(), 0)

    def test_rbt_size_r_one(self):
        rbt = get_rbt_from_list(data_one)
        self.assertEqual(rbt.bst_get_size_r(), len(data_one))

    def test_rbt_size_r_two(self):
        rbt = get_rbt_from_list(data_left)
        self.assertEqual(rbt.bst_get_size_r(), len(data_left))

    def test_rbt_size_r_three(self):
        rbt = get_rbt_from_list(test_list)
        self.assertEqual(rbt.bst_get_size_r(), len(test_list))

    def test_rbt_insert_nr(self):
        lst = generate_random_list(99, 1, 999)
        bst = get_bst_from_list(lst)
        rbt = get_rbt_from_list(lst)
        self.assertEqual(bst.bst_get_size_r(), rbt.bst_get_size_r())
        self.assertEqual(bst.bst_get_size_nr(), rbt.bst_get_size_nr())
        self.assertEqual(bst.bst_inorder_list_r(), rbt.bst_inorder_list_r())
        self.assertEqual(bst.bst_inorder_list_nr(), rbt.bst_inorder_list_nr())
        print (rbt.bst_inorder_list_nr())

if __name__ == '__main__':
    print ("Running UT cases for rb_tree.\n")
    unittest.main()





