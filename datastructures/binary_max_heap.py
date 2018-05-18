#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : binary_max_heap.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Implementation of Binary Min-Heap
# ---------------------------------------------------------------------

from algorithms.binary_heap import binary_heap


class binary_max_heap(binary_heap):
    def __init__(self, alist):
        super(binary_max_heap, self).__init__()
        if len(alist):
            if len(set([type(x) for x in alist])) > 1:
                raise Exception('binary_max_heap::multiple data types are not supported')

            self.h_size = len(alist)
            self.h_list += alist[:]
            idx = len(alist) // 2
            while idx > 0:
                self._shift_down(idx)
                idx -= 1

    def _shift_up(self, idx):
        # while item at parent idx is smaller than item and current idx,
        # move current item up and bring down parent item.
        parent_idx = self.parent_idx(idx)
        while parent_idx > 0:
            if self.value_at(parent_idx) < self.value_at(idx):
                self._swap_two_at(parent_idx, idx)
                parent_idx = self.parent_idx(parent_idx)
            else:
                break

    def _shift_down(self, idx):
        # while the node at idx has a left child (and right child), do this;
        # see if any of its children are greater than itself and if so push
        # this node down and bring-up the greater child.
        while self.lchild_idx(idx) <= self.h_size:
            # check if also has a right child.
            # if so, consider the maximum of both children
            lc_idx = self.lchild_idx(idx)
            rc_idx = self.rchild_idx(idx)
            if rc_idx <= self.h_size:
                max_child_idx = lc_idx if self.value_at(lc_idx) > self.value_at(rc_idx) else rc_idx
            else:
                max_child_idx = lc_idx
            if self.value_at(idx) < self.value_at(max_child_idx):
                self._swap_two_at(idx, max_child_idx)
                idx = max_child_idx
            else:
                break

    def max_heap_get_max(self):
        return self.value_at(1) if self.h_size else None

    def max_heap_insert(self, key):
        if self.h_size and not isinstance(key, type(self.h_list[1])):
            raise Exception('binary_max_heap::multiple data types are not supported')
        self.h_list.append(key)
        self.h_size += 1
        parent_idx = self.parent_idx(self.h_size)
        if self.value_at(parent_idx) < self.value_at(self.h_size):
            self._shift_up(self.h_size)

    def max_heap_extract(self):
        ret_val= self.value_at(1)
        self.h_list[1] = self.value_at(self.h_size)
        self.h_size -= 1
        self.h_list.pop()
        self._shift_down(1)
        return ret_val

    def max_heap_sort(self):
        ret = []
        for idx in xrange(1, self.h_size + 1):
            ret.append(self.max_heap_extract())
        return ret

