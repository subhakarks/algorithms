#!/usr/bin/env python

# ---------------------------------------------------------------------
# File Name : stack_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for stack implementation
# ---------------------------------------------------------------------


import unittest
from algorithms.stack import stack
from algorithms.tests.common import generate_random_list

class stack_tests(unittest.TestCase):
    def test_stk_empty(self):
        stk = stack()
        self.assertEqual(0, stk.stk_get_len())
        self.assertEqual(None, stk.stk_top())
        self.assertEqual(None, stk.stk_pop())
        self.assertEqual(True, stk.stk_isempty())
        with self.assertRaises(Exception) as cm:
            stk.stk_peek(0)
        self.assertEqual(cm.exception.message, "stack::index is out of range")

    def test_stk_size0(self):
        with self.assertRaises(Exception) as cm:
            stk = stack(0)
        self.assertEqual(cm.exception.message, "stack::invalid stack size")

    def test_stk_size1(self):
        s = stack(1)
        s.stk_push(9)
        self.assertEqual(1, s.stk_get_len())
        self.assertEqual(9, s.stk_pop())
        self.assertEqual(None, s.stk_pop())
        s.stk_push(9)
        with self.assertRaises(Exception) as cm:
            s.stk_push(10)
        self.assertEqual(cm.exception.message, "stack::stack is full")

    def test_stk_reverse(self):
        lst = generate_random_list(9, 1, 99)
        stk = stack()
        for x in xrange(0, len(lst)):
            stk.stk_push(lst[x])
        ret = []
        while not stk.stk_isempty():
            ret.append(stk.stk_pop())
        lst.reverse()
        self.assertEqual(lst, ret)

    def test_stk_full(self):
        stk = stack(2)
        stk.stk_push(1)
        stk.stk_push(2)
        self.assertEqual(True, stk.stk_isfull())
        stk.stk_pop()
        self.assertEqual(False, stk.stk_isfull())


if __name__ == '__main__':
    print ("Running UT cases for stack\n")
    unittest.main()
