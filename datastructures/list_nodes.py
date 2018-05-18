#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : list_nodes.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Definitions for List nodes.
#
# ---------------------------------------------------------------------

class slist_node(object):
    def __init__(self, data=None):
        self.data = data
        self.nxt = None

    def __del__(self):
        self.nxt = None

class dlist_node(slist_node):
    def __init__(self, data=None):
        super(dlist_node, self).__init__(data)
        self.prv = None

    def __del__(self):
        super(dlist_node, self).__del__()
        self.prv = None

clist_node = slist_node
