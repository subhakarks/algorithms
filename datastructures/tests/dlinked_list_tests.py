#!/usr/bin/env python
#---------------------------------------------------------------------
# File Name : dlinked_list_tests.py
# Author    : Subhakar K S
#---------------------------------------------------------------------
# Description:
# Test cases for doubly linked lists
#---------------------------------------------------------------------

from algorithms.dlinked_list import dlinked_list
from algorithms.tests.common import generate_random_list

import unittest
import random

class dlinked_list_tests(unittest.TestCase):
    def test_dlist_empty(self):
        dl = dlinked_list()
        self.assertEqual(0, dl.dlist_get_len())
        self.assertEqual(None, dl.dlist_find_item(9))
        self.assertEqual([], dl.dlist_get_as_list())
        self.assertEqual([], dl.dlist_get_as_reverse_list())


    def test_dlist_one_item(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        self.assertEqual(1, dl.dlist_get_len())
        self.assertEqual(None, dl.dlist_find_item(9))
        self.assertEqual(3, dl.dlist_find_item(3))
        self.assertEqual([3], dl.dlist_get_as_list())
        self.assertEqual([3], dl.dlist_get_as_reverse_list())

    def test_dlist_two_items(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        dl.dlist_insert(6)
        self.assertEqual(2, dl.dlist_get_len())
        self.assertEqual(None, dl.dlist_find_item(9))
        self.assertEqual(3, dl.dlist_find_item(3))
        self.assertEqual(6, dl.dlist_find_item(6))
        self.assertEqual([3,6], dl.dlist_get_as_list())
        self.assertEqual([6,3], dl.dlist_get_as_reverse_list())

    def test_dlist_delete_4_items(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        dl.dlist_insert(6)
        dl.dlist_insert(9)
        dl.dlist_insert(12)
        dl.dlist_delete(3)
        self.assertEqual([3,6,12], dl.dlist_get_as_list())
        dl.dlist_delete(2)
        self.assertEqual([3,12], dl.dlist_get_as_list())

    def test_dlist_delete1(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        dl.dlist_delete_item(3)
        self.assertEqual([], dl.dlist_get_as_list())

    def test_dlist_delete2(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        dl.dlist_insert(6)
        dl.dlist_delete_item(6)
        self.assertEqual([3], dl.dlist_get_as_list())

    def test_dlist_delete3(self):
        dl = dlinked_list()
        dl.dlist_insert(3)
        dl.dlist_insert(6)
        dl.dlist_insert(9)
        dl.dlist_delete_item(6)
        self.assertEqual([3,9], dl.dlist_get_as_list())


if __name__ == '__main__':
    print ("Running UT cases for dlinked_list\n")
    unittest.main()



