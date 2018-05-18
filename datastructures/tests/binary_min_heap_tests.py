#!/usr/bin/env python

# ---------------------------------------------------------------------
# File Name : binary_min_heap_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for Binary Min-Heap implementation
# ---------------------------------------------------------------------


import unittest
from algorithms.binary_min_heap import binary_min_heap
from algorithms.tests.common import generate_random_list

data_one = [9]
data_left = [9, 6, 3]
data_right = [3, 6, 9]
data_center = [6, 3, 9]
ascend = [3, 6, 9]
descend = [9, 6, 3]
test_list = [81, 54, 90, 36, 69, 136, 45, 63, 89, 96]
test_list2 = [81, 54, 90, 136, 89, 94, 69, 36, 45, 63, 65, 61]


class binary_min_heap_tests(unittest.TestCase):
    def test_min_heap_data_1(self):
        mh = binary_min_heap(data_one)
        mh.min_heap_insert(3)
        data = mh.min_heap_extract()
        self.assertEqual(3, data)
        tlist = mh.min_heap_sort()
        self.assertEqual(tlist, data_one)

    def test_min_heap_data_2(self):
        mh = binary_min_heap(data_one)
        data = mh.min_heap_extract()
        self.assertEqual(9, data)
        tlist = mh.min_heap_sort()
        self.assertEqual(tlist, [])

    def test_min_heap_data_left(self):
        mh = binary_min_heap(data_left)
        tlist = data_left[:]
        tlist.sort()
        data = mh.min_heap_get_min()
        self.assertEqual(3, data)
        self.assertEqual(tlist, mh.min_heap_sort())

    def test_min_heap_data_right(self):
        mh = binary_min_heap(data_right)
        tlist = data_right[:]
        tlist.sort()
        data = mh.min_heap_get_min()
        self.assertEqual(3, data)
        self.assertEqual(tlist, mh.min_heap_sort())

    def test_min_heap_1(self):
        mh = binary_min_heap(test_list)
        slist = test_list[:]
        slist.sort()
        for i in xrange(len(slist)):
            mh_min = mh.min_heap_extract()
            self.assertEqual(slist[i], mh_min)

    def test_min_heap_2(self):
        mh = binary_min_heap(test_list2)
        slist = test_list2[:]
        slist.sort()
        ret = mh.min_heap_sort()
        self.assertEqual(ret, slist)

    def test_min_heap_min(self):
        test_data = generate_random_list(9, 1, 49)
        mh = binary_min_heap(test_data)
        test_data.sort()
        self.assertEqual(test_data[0], mh.min_heap_get_min())

    def test_min_heap_min_2(self):
        test_data = generate_random_list(18, 1, 999)
        mh = binary_min_heap(test_data)
        test_data.sort()
        self.assertEqual(test_data[0], mh.min_heap_get_min())
        ret = mh.min_heap_sort()
        self.assertEqual(test_data, ret)

    def test_min_heap_min_3(self):
        test_data = [6, 4, 1, 9, 5, 2]
        mh = binary_min_heap(test_data)
        test_data.sort()
        self.assertEqual(test_data[0], mh.min_heap_get_min())

    def test_min_heap_4(self):
        mh = binary_min_heap([])
        mh.min_heap_insert(3)
        ret = mh.min_heap_extract()
        self.assertEqual(ret, 3)

    def test_min_heap_type_1(self):
        with self.assertRaises(Exception) as cm:
            mh = binary_min_heap([1, 2, '3'])
        self.assertEqual(cm.exception.message,
                         'binary_min_heap::multiple data types are not supported')

    def test_min_heap_type_2(self):
        mh = binary_min_heap([9])
        with self.assertRaises(Exception) as cm:
            mh.min_heap_insert('abc')
        self.assertEqual(cm.exception.message,
                         'binary_min_heap::multiple data types are not supported')


if __name__ == '__main__':
    print ("Running UT cases for binary_min_heap \n")
    unittest.main()





