#!/usr/bin/env python

# ---------------------------------------------------------------------
# File Name : queue_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for queue implementation
# ---------------------------------------------------------------------


import unittest
from algorithms.queue import queue
from algorithms.tests.common import generate_random_list

class queue_tests(unittest.TestCase):
    def test_que_empty(self):
        que = queue()
        self.assertEqual(0, que.que_get_len())
        self.assertEqual(True, que.que_isempty())
        self.assertEqual(False, que.que_isfull())
        self.assertEqual(None, que.que_front())
        self.assertEqual(None, que.que_rear())
        self.assertEqual(None, que.que_deque())

    def test_que_size0(self):
        with self.assertRaises(Exception) as cm:
            que = queue(0)
        self.assertEqual(cm.exception.message, "queue::invalid queue size")

    def test_que_size1(self):
        que = queue(1)
        que.que_enque(9)
        self.assertEqual(1, que.que_get_len())
        self.assertEqual(True, que.que_isfull())
        self.assertEqual(9, que.que_front())
        self.assertEqual(9, que.que_rear())
        with self.assertRaises(Exception) as cm:
            que.que_enque(10)
        self.assertEqual(cm.exception.message, "queue::queue is full")
        self.assertEqual(9, que.que_deque())

    def test_que_list(self):
        lst = generate_random_list(9, 1, 99)
        que = queue()
        for x in xrange(0, len(lst)):
            que.que_enque(lst[x])
        ret = []
        self.assertEqual(lst[0], que.que_front())
        self.assertEqual(lst[-1], que.que_rear())
        while not que.que_isempty():
            ret.append(que.que_deque())
        self.assertEqual(ret, lst)


if __name__ == '__main__':
    print ("Running UT cases for queue\n")
    unittest.main()
