#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : queue.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# queue implementation
# ---------------------------------------------------------------------

INFINITE = 999


class queue(object):
    def __init__(self, size=INFINITE):
        if size < 1:
            raise Exception('queue::invalid queue size')
        self.que = []
        self.que_size = size

    def que_get_size(self):
        return self.que_size

    def que_get_len(self):
        return len(self.que)

    def que_isempty(self):
        return False if len(self.que) else True

    def que_isfull(self):
        return True if len(self.que) == self.que_size else False

    def que_enque(self, item):
        if len(self.que) < self.que_size:
            self.que.append(item)
            return item
        else:
            raise Exception('queue::queue is full')

    def que_deque(self):
        if not len(self.que):
            return None
        return self.que.pop(0)

    def que_front(self):
        if not len(self.que):
            return None
        return self.que[0]

    def que_rear(self):
        if not len(self.que):
            return None
        return self.que[-1]


if __name__ == '__main__':
    pass





