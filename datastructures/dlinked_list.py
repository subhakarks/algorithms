#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : dlinked_list.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Doubly linked list implementation
# ---------------------------------------------------------------------

from algorithms.list_nodes import dlist_node

class dlinked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def dlist_get_len(self):
        return self.count

    def dlist_get_as_list(self):
        if not self.head:
            return []
        ret = []
        trav = self.head
        while trav:
            ret.append(trav.data)
            trav = trav.nxt
        return ret

    def dlist_get_as_reverse_list(self):
        if not self.head:
            return []
        trav = self.tail
        ret = []
        while trav:
            ret.append(trav.data)
            trav = trav.prv
        return ret

    def dlist_insert(self, item, pos=-1):
        """
        Default position of pos = -1 implies
        insert item at end of the list.
        """
        if not item:
            raise Exception('dlist::invalid of None item')
        node = dlist_node(item)
        if 1 == pos:
            if not self.head:
                self.head = self.tail = node
            else:
                node.nxt = self.head
                self.head.prv = node
                self.head = node
        elif -1 == pos:
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.nxt = node
                node.prv = self.tail
                self.tail = node
        elif 1 > pos > self.count:
            raise Exception('dlist::invalid position specified')
        else:
            num = 1
            trav = self.head
            while num < (pos-1):
                trav = trav.nxt
                num += 1
            node.nxt = trav.next
            node.prv = trav
            trav.nxt = node
            node.nxt.prv = node

        self.count += 1
        return item

    def dlist_delete(self, pos=-1):
        """
        Default position of pos = -1 implies
        insert item at end of the list.
        """
        if 0 == self.count:
            raise Exception("dlist::cannot delete from an empty list")

        if 1 > pos > self.count:
            raise Exception("dlist::invalid position specified")

        if 1 == self.count and pos in (-1, 1):
            del_node = self.head
            self.head = self.tail = None
            self.count = 0
            del del_node
            return True

        if 1 == pos:
            del_node = self.head
            self.head = self.head.nxt
            self.head.prv = None
        elif pos in (-1, self.count):
            del_node = self.tail
            self.tail = self.tail.prv
            self.tail.nxt = None
        else:
            num = 1
            trav = self.head
            while num < pos:
                trav = trav.nxt
                num += 1
            del_node = trav
            trav.prv.nxt = trav.nxt
            trav.nxt.prv = trav.prv

        del del_node
        self.count -= 1
        return True

    def dlist_append_iterable(self, iter):
        if not hasattr(iter, '__iter__'):
            raise Exception('dlist::input is not an iterable')

        for item in iter:
            self.dlist_insert(item)
        return True

    def dlist_find_item(self, item):
        if not item:
            raise Exception('dlist::invalid or None item')
        trav = self.head
        while trav:
            if trav.data == item:
                return trav.data
            trav = trav.nxt
        return None

    def dlist_delete_item(self, item):
        if not item:
            raise Exception('dlist::invalid or None item')

        del_node = None
        if item == self.head.data:
            del_node = self.head
            self.head.prv = None
            self.head = self.head.nxt
        elif item == self.tail.data:
            del_node = self.tail
            self.tail = self.tail.prv
            self.tail.nxt = None
        else:
            trav = self.head
            while trav:
                if item == trav.data:
                    break
                trav = trav.nxt
            if trav:
                del_node = trav
                trav.nxt.prv = trav.prv
                trav.prv.nxt = trav.nxt

        if del_node:
            del del_node
            self.count -= 1
            return True

        return False




