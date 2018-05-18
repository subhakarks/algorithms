#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : avl_tree.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description: 
# Balanced Binary Trees
# ---------------------------------------------------------------------

from algorithms.binary_tree import btree_node
from algorithms.binary_search_tree import binary_search_tree

class avl_node(btree_node):
    def __init__(self, data=None):
        super(avl_node, self).__init__(data)
        self.ht = 0

    def __del__(self):
        super(avl_node, self).__del__()
        self.ht = 0

class avl_tree(binary_search_tree):
    def __init__(self, from_list=None):
        super(avl_tree, self).__init__(from_list)

if __name__ == '__main__':
    pass



