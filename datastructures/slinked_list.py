#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : slinked_list.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# single linked list implementation
# ---------------------------------------------------------------------

from algorithms.list_nodes import slist_node

class slinked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def slist_get_len(self):
        return self.count

    def slist_get(self, pos=-1):
        if 0 == self.count:
            raise Exception('slist::linked list is empty')

        if 1 > pos > self.count:
           raise Exception('slist::invalid pos specified')

        if 1 == pos:
            return self.head.data
        elif pos in (-1, self.count):
            return self.tail.data
        else:
            num = 1
            trav = self.head
            while num < pos:
                trav = trav.nxt
                num += 1
            return trav.data

    def slist_get_as_list(self):
        ret = []
        if not self.head:
            return ret
        trav = self.head
        while trav:
            ret.append(trav.data)
            trav = trav.nxt
        return ret

    def slist_insert(self, item, pos=-1):
        """
        Default position of pos = -1 implies
        insert item at end of the list.
        """
        if not item:
            raise Exception('slist::invalid or None item')

        node = slist_node(item)
        if 1 == pos:
           if not self.head:
               self.head = self.tail = node
           else:
               node.nxt = self.head
               self.head = node
        elif -1 == pos:
           if not self.head:
               self.head = self.tail = node
           else:
               self.tail.nxt = node
               self.tail = node
        elif 1 > pos > self.count:
            raise Exception('slist::invalid position specified')
        else:
            num = 1
            trav = self.head
            while num < (pos-1):
                trav = trav.nxt
                num += 1
            node.nxt = trav.nxt
            trav.nxt = node

        self.count += 1
        return item

    def slist_delete(self, pos=-1):
        """
        Default position of pos = -1 implies
        delete item from end of the list.
        """
        if 0 == self.count:
            raise Exception("slist::cannot delete from an empty list")

        if 1 > pos > self.count:
            raise Exception("slist::invalid position specified")

        if 1 == self.count and pos in (-1, 1):
            del_node = self.head
            self.head = self.tail = None
            self.count = 0
            del del_node
            return True

        if 1 == pos:
            del_node = self.head
            self.head = self.head.nxt
        elif pos in (-1, self.count):
           trav = self.head
           while self.tail != trav.nxt:
               trav = trav.nxt
           del_node = trav.nxt
           trav.nxt = None
           self.tail = trav
        else:
            num = 1
            prev = None
            trav = self.head
            while num < pos:
                prev = trav
                trav = trav.nxt
                num += 1
            del_node = trav
            prev.nxt = trav.nxt

        del del_node
        self.count -= 1
        return True

    def slist_append_iterable(self, iter):
        if not hasattr(iter, '__iter__'):
            raise Exception('slist::input is not an iterable')

        for item in iter:
            self.slist_insert(item)
        return True

    def slist_find_item(self, item):
        if not item:
            raise Exception('slist::invalid or None item')
        trav = self.head
        pos = 1
        while trav:
            if trav.data == item:
                return pos
            trav = trav.nxt
            pos += 1
        return None

    def slist_delete_item(self, item):
        if not item:
            raise Exception('slist::invalid or None item')
        if item == self.head.data:
            del_node = self.head
            self.head = self.head.nxt
        elif item == self.tail.data:
            trav = self.head
            while trav.nxt != self.tail:
                trav = trav.nxt
            del_node = trav.nxt
            self.tail = trav
        else:
            trav = self.head
            while item != trav.nxt.data:
                trav = trav.nxt
            del_node = trav.nxt
            trav.nxt = trav.nxt.nxt

        if del_node:
            del del_node
            self.count -= 1
            return True

        return False

    def slist_reverse(self):
        trav = self.head
        self.tail = self.head
        prv = None
        while trav:
            nxt = trav.nxt
            trav.nxt = prv
            prv = trav
            trav = nxt
        self.head = prv
        return

