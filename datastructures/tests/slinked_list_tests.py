#!/usr/bin/env python
#---------------------------------------------------------------------
# File Name : slinked_list_tests.py
# Author    : Subhakar K S
#---------------------------------------------------------------------
# Description:
# Test cases for single linked lists
#---------------------------------------------------------------------

from algorithms.slinked_list import slinked_list

import unittest

class slinked_list_tests(unittest.TestCase):
    def test_slist_empty(self):
        slist = slinked_list()
        self.assertEqual(0, slist.slist_get_len())
        self.assertEqual(None, slist.slist_find_item(9))
        self.assertEqual([], slist.slist_get_as_list())

    def test_slist_from_list(self):
        slist = slinked_list()
        lst = range(1, 10)
        slist.slist_append_iterable(lst)
        self.assertEqual(len(lst), slist.slist_get_len())
        self.assertEqual(lst, slist.slist_get_as_list())

    def test_slist_from_tuple(self):
        slist = slinked_list()
        tup = tuple(range(1, 10))
        slist.slist_append_iterable(tup)
        self.assertEqual(len(tup), slist.slist_get_len())
        self.assertEqual(list(tup), slist.slist_get_as_list())

    def test_slist_from_set(self):
        slist = slinked_list()
        new = set(range(1, 10))
        slist.slist_append_iterable(new)
        self.assertEqual(len(new), slist.slist_get_len())
        self.assertEqual(list(new), slist.slist_get_as_list())

    def test_slist_append_from_list(self):
        slist = slinked_list()
        res = range(1, 10)
        new = range(1, 5)
        slist.slist_append_iterable(new)
        new = range(5, 10)
        slist.slist_append_iterable(new)
        self.assertEqual(len(res), slist.slist_get_len())
        self.assertEqual(res, slist.slist_get_as_list())

    def test_slist_get_item1(self):
        slist = slinked_list()
        slist.slist_insert(9)
        self.assertEqual(9, slist.slist_get())
        self.assertEqual(9, slist.slist_get(1))
        self.assertEqual(9, slist.slist_get(-1))
        self.assertEqual(9, slist.slist_get(slist.slist_get_len()))

    def test_slist_get_item2(self):
        slist = slinked_list()
        slist.slist_insert(6)
        slist.slist_insert(9)
        self.assertEqual(9, slist.slist_get())
        self.assertEqual(6, slist.slist_get(1))
        self.assertEqual(9, slist.slist_get(-1))
        self.assertEqual(9, slist.slist_get(slist.slist_get_len()))

    def test_slist_get_item3(self):
        slist = slinked_list()
        slist.slist_insert(3)
        slist.slist_insert(6)
        slist.slist_insert(9)
        self.assertEqual(3, slist.slist_get(1))
        self.assertEqual(6, slist.slist_get(2))
        self.assertEqual(9, slist.slist_get(3))
        self.assertEqual(9, slist.slist_get())
        self.assertEqual(9, slist.slist_get(-1))
        self.assertEqual(9, slist.slist_get(slist.slist_get_len()))

    def test_slist_insert_item1(self):
        slist = slinked_list()
        slist.slist_insert(9)
        slist.slist_insert(6)
        slist.slist_insert(3)
        self.assertEqual([9,6,3],
                         slist.slist_get_as_list())

    def test_slist_insert_item3(self):
        slist = slinked_list()
        slist.slist_insert(3)
        slist.slist_insert(9)
        slist.slist_insert(6, 2)
        self.assertEqual([3, 6, 9],
                         slist.slist_get_as_list())

    def test_slist_delete_4_items(self):
        sl = slinked_list()
        sl.slist_insert(3)
        sl.slist_insert(6)
        sl.slist_insert(9)
        sl.slist_insert(12)
        sl.slist_delete(3)
        self.assertEqual([3,6,12], sl.slist_get_as_list())
        sl.slist_delete(2)
        self.assertEqual([3,12], sl.slist_get_as_list())

    def test_slist_delete_item(self):
        sl = slinked_list()
        sl.slist_insert(3)
        sl.slist_insert(6)
        sl.slist_insert(9)
        sl.slist_delete_item(6)
        self.assertEqual([3,9], sl.slist_get_as_list())

    def test_slist_reverse1(self):
        sl = slinked_list()
        sl.slist_insert(3)
        sl.slist_reverse()
        self.assertEqual([3], sl.slist_get_as_list())

    def test_slist_reverse2(self):
        sl = slinked_list()
        sl.slist_insert(3)
        sl.slist_insert(6)
        sl.slist_reverse()
        self.assertEqual([6,3], sl.slist_get_as_list())

    def test_slist_reverse3(self):
        sl = slinked_list()
        sl.slist_insert(3)
        sl.slist_insert(6)
        sl.slist_insert(9)
        sl.slist_reverse()
        self.assertEqual([9,6,3], sl.slist_get_as_list())


if __name__ == '__main__':
    print ("Running UT cases for slinked_list\n")
    unittest.main()



