#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : clinked_list.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Circular linked list implementation
# ---------------------------------------------------------------------

from algorithms.list_nodes import clist_node

class clinked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def clist_get_len(self):
        return self.count

