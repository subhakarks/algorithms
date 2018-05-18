#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : binary_heap.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Base class for binary heap implementations.
# ---------------------------------------------------------------------

class binary_heap(object):
    value_at = lambda self, x: self.h_list[x]
    parent_idx = lambda self, x: x // 2
    lchild_idx = lambda self, x: 2 * x
    rchild_idx = lambda self, x: (2 * x) + 1

    def __init__(self):
        self.h_list = [None]
        self.h_size = 0

    def _swap_two_at(self, idx1, idx2):
        (self.h_list[idx1], self.h_list[idx2]) = (self.h_list[idx2], self.h_list[idx1])
