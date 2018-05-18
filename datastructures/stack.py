#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : stack.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Stack implementation
# ---------------------------------------------------------------------

INFINITE = 999


class stack(object):
    def __init__(self, size=INFINITE):
        if size < 1:
            raise Exception('stack::invalid stack size')
        self.stk = []
        self.stk_size = size

    def stk_get_size(self):
        return self.stk_size

    def stk_get_len(self):
        return len(self.stk)

    def stk_isempty(self):
        return False if len(self.stk) else True

    def stk_isfull(self):
        return True if len(self.stk) == self.stk_size else False

    def stk_push(self, item):
        if len(self.stk) < self.stk_size:
            self.stk.append(item)
            return item
        else:
            raise Exception('stack::stack is full')

    def stk_pop(self):
        if not len(self.stk):
            return None
        return self.stk.pop()

    def stk_top(self):
        if not len(self.stk):
            return None
        return self.stk[-1]

    def stk_peek(self, pos):
        if 0 <= pos <= (len(self.stk) - 1):
            return self.stk[pos]
        else:
            raise Exception('stack::index is out of range')

    def __str__(self):
        str = "Object Information:\n"
        str += "Class : %s\n" % self.__class__.__name__
        str += "Base  : %s\n" % self.__class__.__bases__
        str += "Addr  : %s\n" % (hex(id(self)))
        str += "Data  : (%d) elements\n" % len(self.stk)
        str += list.__str__(self)
        return str


if __name__ == '__main__':
    pass

