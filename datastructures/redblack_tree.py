#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : redblack_tree.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description: 
# Red Black tree implementation
# RBT Rules:
# - Every node is marked RED or BLACK
# - Root is always BLACK
# - No two consecutive nodes in a path can be RED
# - Every path from root to leaf has same number of BLACKs
# - Newly inserted are nodes are marked RED
# - Null nodes are treated BLACK
# ---------------------------------------------------------------------

from algorithms.binary_tree import btree_node
from algorithms.binary_search_tree import binary_search_tree

RED = True
BLACK = False

class rbtree_node(btree_node):
    def __init__(self, data=None):
        super(rbtree_node, self).__init__(data)
        self.parent = None
        self.color = RED

    def __del__(self):
        super(rbtree_node, self).__del__()
        self.parent = None
        self.color = RED


class rb_tree(binary_search_tree):
    def __init__(self, from_list=None):
        super(rb_tree, self).__init__(from_list)

    def _get_new_node(self, item):
        return rbtree_node(item)

    def _rbt_rotate_left(self, node):
        rite = node.r_child
        node.r_child = rite.l_child
        if node.r_child is not None:
            node.r_child.parent = node
        rite.parent = node.parent
        if node.parent is None:
            self.root = rite
        elif node == node.parent.l_child:
            node.parent.l_child = rite
        else:
            node.parent.r_child = rite
        rite.l_child = node
        node.parent = rite
        return

    def _rbt_rotate_right(self, node):
        lft = node.l_child
        node.l_child = lft.r_child
        if node.l_child is not None:
            node.l_child.parent = node
        lft.parent = node.parent
        if node.parent is None:
            self.root = lft
        elif node == node.parent.l_child:
            node.parent.l_child = lft
        else:
            node.parent.r_child = lft
        lft.r_child = node
        node.parent = lft
        return

    def _rbt_fix_violations(self, node):
        """
        check if new node's aunt's color.
        If
        - BLACK aunt: Rotate
        - RED aunt: re-color

        """
        while (node != self.root and BLACK != node.color and
               RED == node.parent.color):
            parent = node.parent
            g_parent = node.parent.parent

            if parent == g_parent.l_child:
                aunt = g_parent.r_child
                if aunt and RED == aunt.color:
                    # RED aunt implies re-coloring
                    g_parent.color = RED
                    parent.color = BLACK
                    aunt.color = BLACK
                    node = g_parent
                else:
                    # BLACK aunt or None(treated BLACK) implies rotations
                    if node == parent.r_child:
                        self._rbt_rotate_left(parent)
                        node = parent
                        parent = node.parent

                    self._rbt_rotate_right(g_parent)
                    parent.color, g_parent.color = g_parent.color, parent.color
                    node = parent
            else:
                aunt = g_parent.l_child
                if aunt and RED == aunt.color:
                    g_parent.color = RED
                    parent.color = BLACK
                    aunt.color = BLACK
                    node = g_parent
                else:
                    if node == parent.l_child:
                        self._rbt_rotate_right(parent)
                        node = parent
                        parent = node.parent
                    self._rbt_rotate_left(g_parent)
                    parent.color, g_parent.color = g_parent.color, parent.color
                    node = parent

        self.root.color = BLACK
        return True

    def rbt_insert_nr(self, item):
        if not item:
            return None
        node = self._get_new_node(item)
        if not self.root:
            self.root = node
            node.color = BLACK
            return item

        trav = self.root
        prev = self.root
        while trav:
            prev = trav
            if item < trav.data:
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
            elif item == trav.data:
                return item
        # found the place to insert new node.
        # determine if it should be inserted as left child or right
        if prev.data > item:
            prev.l_child = node
        else:
            prev.r_child = node
        node.parent = prev

        self._rbt_fix_violations(node)


if __name__ == '__main__':
    pass



