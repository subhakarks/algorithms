#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : binary_search_tree.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description: 
# Binary Search Tree implementation
# ---------------------------------------------------------------------
from algorithms.binary_tree import btree_node, binary_tree
from algorithms.stack import stack
from algorithms.queue import queue

class binary_search_tree(binary_tree):
    def __init__(self, from_list=None):
        super(binary_search_tree, self).__init__()
        if not from_list:
            return
        for item in from_list:
            self.bst_insert_r(item)

    # -------------- recursive algorithms ------------------
    def _get_new_node(self, item):
        return btree_node(item)

    def _get_size_r(self, node):
        if not node:
            return 0
        return 1 + self._get_size_r(node.l_child) + self._get_size_r(node.r_child)

    def bst_get_size_r(self):
        return self._get_size_r(self.root)

    def _max_height_r(self, node):
        if not node:
            return 0
        l_max = self._max_height_r(node.l_child)
        r_max = self._max_height_r(node.r_child)

        ret = l_max if l_max > r_max else r_max
        return ret+1

    def bst_get_height_r(self):
        return self._max_height_r(self.root)

    def _insert_r(self, head, new):
        if new.data < head.data:
            if head.l_child is None:
                head.l_child = new
            else:
                return self._insert_r (head.l_child, new)
        elif new.data > head.data:
            if head.r_child is None:
                head.r_child = new
            else:
                return self._insert_r (head.r_child, new)

        return new.data

    def bst_insert_r(self, item):
        if not item:
            return None
        node = self._get_new_node(item)
        if not self.root:
            self.root = node
            return item

        return self._insert_r(self.root, node)

    def _delete_r(self, parent, node, item):
        if not node:
            return False
        if item < node.data:
            return self._delete_r(node, node.l_child, item)
        elif item > node.data:
            return self._delete_r(node, node.r_child, item)
        else:
            # at the node to be deleted.
            # there are 4 possibilities that this node
            # 1 - has no children
            # 2 - has only left child
            # 3 - has only right child
            # 4 - has both children
            is_left = True if node.data < parent.data else False
            if not node.l_child and not node.r_child:
                if is_left:
                    parent.l_child = None
                else:
                    parent.r_child = None
            elif not node.l_child:
                if is_left:
                    parent.l_child = node.r_child
                else:
                    parent.r_child = node.r_child
            elif not node.r_child:
                if is_left:
                    parent.l_child = node.l_child
                else:
                    parent.r_child = node.l_child
            else:
                # node has both children. follow below logic
                # - find in-order successor ie minimum item in node's right subtree
                # - replace node's data with this minimum item.
                # - delete minimum item from right subtree
                node.data = self._find_min_r(node.r_child)
                self._delete_r(node, node.r_child, node.data)
            return True

    def bst_delete_r(self, item):
        if not item:
            return False
        return self._delete_r(None, self.root, item)

    def _destroy_r(self, node):
        if not node:
            return None
        self._destroy_r(node.l_child)
        self._destroy_r(node.r_child)
        del node
        return True

    def bst_destroy_r(self):
        self._destroy_r(self.root)
        self.root = None

    def _find_r(self, head, item):
        if not head:
            return None

        if head.data == item:
            return True

        if item < head.data:
            return self._find_r(head.l_child, item)

        if item > head.data:
            return self._find_r(head.r_child, item)

    def bst_find_r(self, item):
        if not item:
            return None
        return self._find_r(self.root, item)

    def _find_min_r(self, node):
        if node.l_child is not None:
            return self._find_min_r(node.l_child)
        return node.data

    def bst_find_min_r(self):
        if not self.root:
            return None
        return self._find_min_r(self.root)

    def _find_max_r(self, node):
        if node.r_child is not None:
            return self._find_max_r(node.r_child)
        return node.data

    def bst_find_max_r(self):
        if not self.root:
            return None
        return self._find_max_r(self.root)

    def _inorder_r(self, head, result):
        if not head:
            return 

        if head.l_child:
            self._inorder_r(head.l_child, result)

        result.append(head.data)

        if head.r_child:
            self._inorder_r(head.r_child, result)

        return

    def bst_inorder_list_r(self):
        result = []
        self._inorder_r(self.root, result)
        return result

    def _preorder_r(self, head, result):
        if not head:
            return

        result.append(head.data)

        if head.l_child is not None:
            self._preorder_r(head.l_child, result)

        if head.r_child is not None:
            self._preorder_r(head.r_child, result)

    def bst_preorder_list_r(self):
        result = []
        self._preorder_r(self.root, result)
        return result

    def _postorder_r(self, head, result):
        if not head:
            return

        if head.l_child is not None:
           self._postorder_r(head.l_child, result)

        if head.r_child is not None:
            self._postorder_r(head.r_child, result)

        result.append(head.data)

    def bst_postorder_list_r(self):
        result = []
        self._postorder_r(self.root, result)
        return result

    # --------------------- non-recursive algorithms ---------------------

    def bst_get_size_nr(self):
        if not self.root:
            return 0
        sz = 0
        stk = stack()
        done = False
        trav = self.root
        while not done:
            if trav:
                stk.stk_push(trav)
                trav = trav.l_child
            else:
                if not stk.stk_isempty():
                    trav = stk.stk_pop()
                    sz += 1
                    trav = trav.r_child
                else:
                    done = True
        return sz

    def bst_find_nr(self, item):
        if not item:
            return None

        if not self.root:
            return None

        trav = self.root
        while(trav):
            if trav.data == item:
                return True
            elif item < trav.data :
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
        return False

    def bst_find_get_node_nr(self, item):
        if not item:
            return None

        if not self.root:
            return None

        trav = self.root
        while(trav):
            if trav.data == item:
                return trav
            elif item < trav.data :
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
        return None

    def bst_find_min_nr(self, node=None):
        """
        Finds and returns the node with minimum key in a sub-tree
        headed with node, if key_node is passed.
        If node is None, search starts from root.
        """
        trav = self.root if not node else node

        while trav.l_child:
            trav = trav.l_child
        return trav.data

    def bst_find_max_nr(self, node=None):
        trav = self.root if not node else node

        while trav.r_child:
            trav = trav.r_child
        return trav.data

    def bst_inorder_list_nr(self):
        ret = []
        if not self.root:
            return ret
        done = False
        stk = stack()
        trav = self.root
        while not done:
            if trav:
                stk.stk_push(trav)
                trav = trav.l_child
            else:
                if not stk.stk_isempty():
                    trav = stk.stk_pop()
                    ret.append(trav.data)
                    trav = trav.r_child
                else:
                    done = True
        return ret

    def bst_preorder_list_nr(self):
        ret = []
        if not self.root:
            return ret
        done = False
        stk = stack()
        trav = self.root
        while not done:
            if trav:
                ret.append(trav.data)
                stk.stk_push(trav)
                trav = trav.l_child
            else:
                if not stk.stk_isempty():
                    trav = stk.stk_pop()
                    trav = trav.r_child
                else:
                    done = True
        return ret

    def bst_postorder_list_nr(self):
        """
        Algorithm:
        - Create two stacks, stk1, stk2
        - stk1.push(root)
        - while stk1 is not empty:
              curr = stk1.stk_pop()
              stk2.push(curr)
              if curr has .left:
                 stk1.push(curr.left)
              if curr has right:
                 stk1.push(curr.right)
        - stk2 has all items pushed in post-order.
        """
        ret = []
        if not self.root:
            return ret
        stk1 = stack()
        stk2 = stack()
        stk1.stk_push(self.root)

        while not stk1.stk_isempty():
            curr = stk1.stk_pop()
            stk2.stk_push(curr)
            if curr.l_child:
                stk1.stk_push(curr.l_child)
            if curr.r_child:
                stk1.stk_push(curr.r_child)

        while not stk2.stk_isempty():
            ret.append(stk2.stk_pop().data)

        return ret

    def bst_levelorder_list_nr(self):
        ret = []
        if not self.root:
            return ret
        q = queue()
        q.que_enque(self.root)
        while not q.que_isempty():
            node = q.que_deque()
            ret.append(node.data)
            if node.l_child:
                q.que_enque(node.l_child)
            if node.r_child:
                q.que_enque(node.r_child)
        return ret

    def bst_get_next_inorder_nr(self, item):
        if not self.root:
            return None

        # first, get the node corresponding to this key
        node = self.bst_find_get_node_nr(item)
        if not node:
            return None

        # if key_node has right sub-tree, smallest key in
        # its right sub-tree will be the successor.
        if node.r_child:
            return self.bst_find_min_nr(node.r_child)

        succ = None
        trav = self.root
        while trav:
            if item < trav.data:
                succ = trav
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
            else:
                break
        return succ.data

    def bst_get_next_preorder_nr(self, item):
        if not self.root:
            return None

        # first, get the node corresponding to this key
        node = self.bst_find_get_node_nr(item)
        if not node:
            return None

        # if this node has left child or right child, those
        # will be the next in pre-order traversal
        if node.l_child:
            return node.l_child
        if node.r_child:
            return node.r_child

        # now, we need to bother only about leaf nodes
        stk = stack()
        trav = self.root
        while trav:
            stk.stk_push(trav)
            if item < trav.data:
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
            else:
                break

        prev = stk.stk_pop()
        while not stk.stk_isempty():
            top = stk.stk_top()
            if prev == top.l_child:
                if top.r_child:
                    return top.r_child
            prev = stk.stk_pop()

        return None

    def bst_insert_nr(self, item):
        if not item:
            return None
        node = self._get_new_node(item)
        if not self.root:
            self.root = node
            return item
        trav = prev = self.root
        while trav:
            prev = trav
            if item < trav.data:
                trav = trav.l_child
            elif item > trav.data:
                trav = trav.r_child
            elif item == trav.data:
                return item

        if prev.data > item:
            prev.l_child = node
        else:
            prev.r_child = node
        return item

    def bst_delete_nr(self, item):
        if not item:
            return False

        if not self.root:
            return False

        parent = trav = self.root
        while trav:
            if trav.data < item:
                parent = trav
                trav = trav.r_child
            elif trav.data > item:
                parent = trav
                trav = trav.l_child
            elif trav.data == item:
                # we found the node to be deleted. also determine
                # if this node is left or right child of parent
                is_left = True if trav.data < parent.data else False
                del_node = trav
                # found the required node to be deleted
                # now, we have 4 possibilities:
                # 1 - node does NOT have any children
                # 2 - node has ONLY left child
                # 3 - node has ONLY right child
                # 4 - node has BOTH the children
                if not del_node.l_child and not del_node.r_child:
                    # case-1: node does NOT have any children
                    # so make parent's link (left or right) to this node as None.
                    if is_left:
                        parent.l_child = None
                    else:
                        parent.r_child = None
                elif not del_node.r_child:
                    # case-2: node has ONLY left child
                    # so make it as parent's (left or right) child.
                    if is_left:
                        parent.l_child = del_node.l_child
                    else:
                        parent.r_child = del_node.l_child
                elif not del_node.l_child:
                    # case-3: node has ONLY right child
                    # so make it as parent's (left or right) child.
                    if is_left:
                        parent.l_child = del_node.r_child
                    else:
                        parent.r_child = del_node.r_child
                else:
                    # case-4: node has both left and right child.
                    # we handle this as:
                    #   - find the minimum value in this nodes right sub-tree
                    #   - copy the minimum value from this nodes right sub-tree to this node
                    #   - delete the minimum value from this nodes right sub-tree.
                    # again while finding smallest value on right sub-tree, there are two possibilities
                    #   - (a) right child may not have further left children
                    #     in this case, right child itself is smallest value
                    #   - (b) right child may have further left children
                    #     in this case, smallest value node will not have further lefts, but might have rights

                    trav = trav.r_child
                    if not trav.l_child:
                        # case (a): just copy min-value(ie right child data) to node to be deleted
                        del_node.data = trav.data
                        del_node.r_child = trav.r_child
                        del_node = trav
                    else:
                        # case (b): min-value will be in trav's left subtree.
                        while trav.l_child:
                            parent = trav
                            trav = trav.l_child
                        # reached smallest node on right sub-tree, copy it value to the node to be deleted
                        del_node.data = trav.data
                        parent.l_child = trav.r_child  # may of may not have right child
                        del_node = trav
                del del_node
                return True
        return False

    def bst_destroy_nr(self):
        if not self.root:
            return
        q = queue()
        q.que_enque(self.root)
        while not q.que_isempty():
            del_node = q.que_front()
            q.que_deque()
            if del_node.l_child is not None:
                q.que_enque(del_node.l_child)
            if del_node.r_child is not None:
                q.que_enque(del_node.r_child)
            del del_node
        self.root = None
        return




if __name__ == '__main__':
    pass
