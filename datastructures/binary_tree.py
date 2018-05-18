#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : binary_tree.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description: 
# Binary tree implementation
# ---------------------------------------------------------------------


class btree_node(object):
    def __init__(self, data=None):
        self.r_child = None
        self.l_child = None
        self.data = data

    def __del__(self):
        self.r_child = None
        self.l_child = None
        self.data = None

class binary_tree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        str = "Object Information:\n"
        str += "Class Name: %s\n" % (self.__class__.__name__)
        str += "Base classes: %s\n" % (self.__class__.__bases__)

        return str

if __name__ == '__main__':
    pass



