#!/usr/bin/env python

# ---------------------------------------------------------------------
# File Name : binaryMaxHeap_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for Binary Max-Heap implementation
# ---------------------------------------------------------------------

import unittest
from algorithms.binary_max_heap import binary_max_heap
from algorithms.tests.common import generate_random_list

data_one = [9]
data_left = [9, 6, 3]
data_right = [3, 6, 9]
data_center = [6, 3, 9]
ascend = [3, 6, 9]
descend = [9, 6, 3]
test_list = [81, 54, 90, 36, 69, 136, 45, 63, 89, 96]
test_list2 = [81, 54, 90, 136, 89, 94, 69, 36, 45, 63, 65, 61]


class binary_max_heap_tests(unittest.TestCase):
    def test_max_heap_data_one(self):
        mh = binary_max_heap(data_one)
        mh.max_heap_insert(3)
        data = mh.max_heap_extract()
        self.assertEqual(9, data)
        data = mh.max_heap_extract()
        self.assertEqual(3, data)
        ret = mh.max_heap_sort()
        self.assertEqual(ret, [])

    def test_max_heap_data_left(self):
        mh = binary_max_heap(data_left)
        tlist = data_left[:]
        tlist.sort(reverse=True)
        data = mh.max_heap_get_max()
        self.assertEqual(9, data)
        self.assertEqual(tlist, mh.max_heap_sort())

    def test_max_heap_data_right(self):
        mh = binary_max_heap(data_right)
        tlist = data_right[:]
        tlist.sort(reverse=True)
        data = mh.max_heap_get_max()
        self.assertEqual(9, data)
        self.assertEqual(tlist, mh.max_heap_sort())

    def test_max_heap_1(self):
        mh = binary_max_heap(test_list)
        slist = test_list[:]
        slist.sort(reverse=True)
        for i in xrange(len(slist)):
            mh_max = mh.max_heap_extract()
            self.assertEqual(slist[i], mh_max)

    def test_max_heap_2(self):
        mh = binary_max_heap(test_list2)
        slist = test_list2[:]
        slist.sort(reverse=True)
        ret = mh.max_heap_sort()
        self.assertEqual(ret, slist)

    def test_max_heap_max(self):
        test_data = generate_random_list(9, 1, 49)
        mh = binary_max_heap(test_data)
        test_data.sort(reverse=True)
        self.assertEqual(test_data[0], mh.max_heap_get_max())

    def test_max_heap_max_2(self):
        test_data = [6, 4, 1, 9, 5, 2]
        mh = binary_max_heap(test_data)
        test_data.sort(reverse=True)
        self.assertEqual(test_data[0], mh.max_heap_get_max())


if __name__ == '__main__':
    print ("Running UT cases for binary_max_heap \n")
    unittest.main()

