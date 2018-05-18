#!/usr/bin/env python
# ---------------------------------------------------------------------
# File Name : binary_search_tree_tests.py
# Author    : Subhakar K S
# ---------------------------------------------------------------------
# Description:
# Test cases for Binary Search Tree implementation
#
# ---------------------------------------------------------------------
import unittest
from algorithms.binary_search_tree import binary_search_tree
from algorithms.tests.common import generate_random_list

def get_bst_from_list(bst_list):
    bst = binary_search_tree()
    for ele in bst_list:
        bst.bst_insert_r(ele)
    return  bst

data_one = [9]
data_left = [9, 6, 3]
data_right = [3, 6, 9]
data_center = [6, 3, 9]
ascend = [3, 6, 9]
descend = [9, 6, 3]
test_list = [81, 54, 90, 36, 69, 136, 45, 63, 89, 96]
test_list2 = [81, 54, 90, 136, 89, 94, 69, 36, 45, 63, 65, 61]


class binary_search_treeUnitTests(unittest.TestCase):
    def test_bst_init(self):
        bst = binary_search_tree()
        self.assertEqual(bst.bst_get_size_r(), 0)

    def test_bst_size_r_one(self):
        bst = get_bst_from_list(data_one)
        self.assertEqual(bst.bst_get_size_r(), len(data_one))

    def test_bst_size_r_two(self):
        bst = get_bst_from_list(data_left)
        self.assertEqual(bst.bst_get_size_r(), len(data_left))

    def test_bst_size_r_three(self):
        bst = get_bst_from_list(test_list)
        self.assertEqual(bst.bst_get_size_r(), len(test_list))

    def test_bst_size_nr_one(self):
        bst = get_bst_from_list(data_one)
        self.assertEqual(bst.bst_get_size_nr(), len(data_one))

    def test_bst_size_nr_two(self):
        bst = get_bst_from_list(data_left)
        self.assertEqual(bst.bst_get_size_nr(), len(data_left))

    def test_bst_size_nr_three(self):
        bst = get_bst_from_list(test_list)
        self.assertEqual(bst.bst_get_size_nr(), len(test_list))

    def test_bst_insert_r_nr(self):
        bst_r = binary_search_tree()
        bst_nr = binary_search_tree()
        for i in test_list2:
            bst_r.bst_insert_r(i)
            bst_nr.bst_insert_nr(i)
        self.assertEqual(bst_r.bst_get_size_r(),
                         bst_nr.bst_get_size_nr())
        self.assertEqual(bst_r.bst_inorder_list_r(),
                         bst_nr.bst_inorder_list_nr())

    def test_bst_inorder_one(self):
        bst = get_bst_from_list(data_one)
        in_list = bst.bst_inorder_list_r()
        self.assertEqual(data_one, in_list)

    def test_bst_preorder_one(self):
        bst = get_bst_from_list(data_one)
        pre_list = bst.bst_preorder_list_r()
        self.assertEqual(data_one, pre_list)

    def test_bst_postorder_one(self):
        bst = get_bst_from_list(data_one)
        post_list = bst.bst_postorder_list_r()
        self.assertEqual(data_one, post_list)

    def test_bst_inorder_left(self):
        bst = get_bst_from_list(data_left)
        in_list = bst.bst_inorder_list_r()
        self.assertEqual(ascend, in_list)

    def test_bst_preorder_left(self):
        bst = get_bst_from_list(data_left)
        pre_list = bst.bst_preorder_list_r()
        self.assertEqual(descend, pre_list)

    def test_bst_postorder_left(self):
        bst = get_bst_from_list(data_left)
        post_list = bst.bst_postorder_list_r()
        self.assertEqual(ascend, post_list)

    def test_bst_inorder_right(self):
        bst = get_bst_from_list(data_right)
        in_list = bst.bst_inorder_list_r()
        self.assertEqual(ascend, in_list)

    def test_bst_preorder_right(self):
        bst = get_bst_from_list(data_right)
        pre_list = bst.bst_preorder_list_r()
        self.assertEqual(ascend, pre_list)

    def test_bst_postorder_right(self):
        bst = get_bst_from_list(data_right)
        post_list = bst.bst_postorder_list_r()
        self.assertEqual(descend, post_list)

    def test_bst_inorder_center(self):
        bst = get_bst_from_list(data_center)
        in_list = bst.bst_inorder_list_r()
        self.assertEqual(ascend, in_list)

    def test_bst_inorder_r_nr(self):
        bst = get_bst_from_list(test_list)
        in_r = bst.bst_inorder_list_r()
        in_nr = bst.bst_inorder_list_nr()
        self.assertEqual(in_r, in_nr)

    def test_bst_preorder_r_nr(self):
        bst = get_bst_from_list(test_list)
        r_pre = bst.bst_preorder_list_r()
        nr_pre = bst.bst_preorder_list_nr()
        self.assertEqual(r_pre, nr_pre)

    def test_bst_postorder_r_nr_2stk(self):
        bst = get_bst_from_list(test_list)
        r_post = bst.bst_postorder_list_r()
        nr_post = bst.bst_postorder_list_nr()
        self.assertEqual(r_post, nr_post)

    def test_bst_preorder_center(self):
        bst = get_bst_from_list(data_center)
        pre_list = bst.bst_preorder_list_r()
        self.assertEqual([6, 3, 9], pre_list)

    def test_bst_preorder_random(self):
        pre = [81, 54, 36, 45, 69, 63, 61, 65, 90, 89, 136, 94]
        bst = get_bst_from_list(test_list2)
        r_pre = bst.bst_preorder_list_r()
        nr_pre = bst.bst_preorder_list_nr()
        self.assertEqual(r_pre, nr_pre)
        self.assertEqual(pre, r_pre)
        self.assertEqual(pre, nr_pre)

    def test_bst_postorder_center(self):
        bst = get_bst_from_list(data_center)
        post_list = bst.bst_postorder_list_r()
        self.assertEqual([3, 9, 6], post_list)

    def test_bst_count(self):
        ret = generate_random_list(39, 19, 1000)
        bst = get_bst_from_list(ret)
        count = bst.bst_get_size_r()
        self.assertEqual(len(ret), count)

    def test_bst_min_item_nr(self):
        bst = get_bst_from_list(test_list)
        min_item = bst.bst_find_min_nr()
        self.assertEqual(36, min_item)

    def test_bst_max_item_nr(self):
        bst = get_bst_from_list(test_list)
        max_item = bst.bst_find_max_nr()
        self.assertEqual(136, max_item)

    def test_bst_min_item_r(self):
        bst = get_bst_from_list(test_list)
        min_item = bst.bst_find_min_r()
        self.assertEqual(36, min_item)

    def test_bst_max_item_r(self):
        bst = get_bst_from_list(test_list)
        max_item = bst.bst_find_max_r()
        self.assertEqual(136, max_item)

    def test_bst_max_depth_emtpy_tree_r(self):
        bst = binary_search_tree()
        md = bst.bst_max_depth_r()
        self.assertEqual(0, md)

    def test_bst_max_depth_one_node_r(self):
        bst = get_bst_from_list(data_one)
        md = bst.bst_max_depth_r()
        self.assertEqual(1, md)

    def test_bst_max_depth_3node_r(self):
        bst = get_bst_from_list(data_center)
        md = bst.bst_max_depth_r()
        self.assertEqual(2, md)

    def test_bst_max_depth_3node_left_r(self):
        bst = get_bst_from_list(data_left)
        md = bst.bst_max_depth_r()
        self.assertEqual(3, md)

    def test_bst_max_depth_3node_right_r(self):
        bst = get_bst_from_list(data_right)
        md = bst.bst_max_depth_r()
        self.assertEqual(3, md)

    def test_bst_max_depth_test_list_r(self):
        bst = get_bst_from_list(test_list)
        md = bst.bst_max_depth_r()
        self.assertEqual(4, md)

    def test_bst_delete_from_empty_bst(self):
        bst = binary_search_tree()
        ret = bst.bst_delete_nr(200)
        self.assertEqual(ret, False)
        self.assertEqual(0, bst.bst_get_size_r())

    def test_bst_delete_null_item(self):
        item = None
        bst = get_bst_from_list(test_list)
        bst.bst_delete_nr(item)
        self.assertEqual(len(test_list), bst.bst_get_size_r())

    def test_bst_del_left_leaf_item(self):
        bst = get_bst_from_list(test_list)
        count = bst.bst_get_size_r()
        bst.bst_delete_nr(96)
        self.assertEqual(count-1, bst.bst_get_size_r())

    def test_bst_del_right_leaf_item(self):
        bst = get_bst_from_list(test_list)
        count = bst.bst_get_size_nr()
        bst.bst_delete_nr(45)
        self.assertEqual(count-1, bst.bst_get_size_r())

    def test_bst_del_node_with_only_left_child(self):
        bst = get_bst_from_list(test_list)
        bst.bst_delete_nr(96)
        verify_list = [81, 54, 90, 36, 69, 136, 45, 63, 89]
        verify_bst = get_bst_from_list(verify_list)
        list1 = bst.bst_inorder_list_r()
        list2 = verify_bst.bst_inorder_list_r()
        self.assertEqual(bst.bst_get_size_r(), verify_bst.bst_get_size_r())
        self.assertEqual(len(list1), len(list2))
        self.assertEqual(list1, list2)

    def test_bst_del_node_with_only_right_child(self):
        bst = get_bst_from_list(test_list)
        bst.bst_delete_nr(36)
        verify_list = [81, 54, 90, 69, 136, 45, 63, 89, 96]
        verify_bst = get_bst_from_list(verify_list)
        list1 = bst.bst_inorder_list_r()
        list2 = verify_bst.bst_inorder_list_r()
        self.assertEqual(bst.bst_get_size_r(), verify_bst.bst_get_size_r())
        self.assertEqual(len(list1), len(list2))
        self.assertEqual(list1, list2)

    def test_bst_get_next_inorder_nr(self):
        rlist = generate_random_list(999, 1, 9999)
        bst = get_bst_from_list(rlist)
        rlist.sort()
        for i in xrange(0, len(rlist)-1):
            succ = bst.bst_get_next_inorder_nr(rlist[i])
            self.assertEqual(rlist[i+1], succ)

    def test_bst_get_next_preorder_nr_1(self):
        bst = get_bst_from_list(test_list)
        r_pre = bst.bst_preorder_list_r()

        for i in xrange(len(r_pre)-1):
            succ = bst.bst_get_next_preorder_nr(r_pre[i])
            self.assertEqual(r_pre[i+1], succ.data)
        succ = bst.bst_get_next_preorder_nr(r_pre[-1])
        self.assertEqual(succ, None)

    def test_bst_get_next_preorder_nr_2(self):
        bst = get_bst_from_list(test_list2)
        r_pre = bst.bst_preorder_list_r()

        for i in xrange(len(r_pre)-1):
            succ = bst.bst_get_next_preorder_nr(r_pre[i])
            self.assertEqual(r_pre[i+1], succ.data)
        succ = bst.bst_get_next_preorder_nr(r_pre[-1])
        self.assertEqual(succ, None)


    def test_bst_get_next_preorder_nr_3(self):
        rlist = generate_random_list(999, 1, 9999)
        bst = get_bst_from_list(rlist)
        r_pre = bst.bst_preorder_list_r()
        for i in xrange(len(r_pre)-1):
            succ = bst.bst_get_next_preorder_nr(r_pre[i])
            self.assertEqual(r_pre[i+1], succ.data)
        succ = bst.bst_get_next_preorder_nr(r_pre[-1])
        self.assertEqual(succ, None)

    def test_bst_get_next_preorder_nr_4(self):
        rlist = [9]
        bst = get_bst_from_list(rlist)
        r_pre = bst.bst_preorder_list_r()
        succ = bst.bst_get_next_preorder_nr(r_pre[-1])
        self.assertEqual(succ, None)

    def test_bst_get_next_preorder_nr_5(self):
        rlist = [9, 5]
        bst = get_bst_from_list(rlist)
        r_pre = bst.bst_preorder_list_r()
        succ = bst.bst_get_next_preorder_nr(r_pre[0])
        self.assertEqual(r_pre[1], succ.data)
        succ = bst.bst_get_next_preorder_nr(r_pre[1])
        self.assertEqual(succ, None)

    def test_bst_get_next_preorder_nr_6(self):
        rlist = [9, 19]
        bst = get_bst_from_list(rlist)
        r_pre = bst.bst_preorder_list_r()
        succ = bst.bst_get_next_preorder_nr(r_pre[0])
        self.assertEqual(r_pre[1], succ.data)
        succ = bst.bst_get_next_preorder_nr(r_pre[1])
        self.assertEqual(succ, None)

    def test_bst_del_node_with_two_children_1(self):
        tl = test_list[:]
        bst = get_bst_from_list(tl)
        bst.bst_delete_nr(90)
        tl.remove(90)
        tl.sort()
        vl= bst.bst_inorder_list_r()
        self.assertEqual(tl, vl)

    def test_bst_del_node_with_two_children_2(self):
        tl = test_list[:]
        bst = get_bst_from_list(tl)
        bst.bst_delete_nr(69)
        tl.remove(69)
        tl.sort()
        vl = bst.bst_inorder_list_nr()
        self.assertEqual(tl, vl)

    def test_bst_delete_item(self):
        lst = [17,5,22,2,12,21,36,9,29,44,25,42]
        bst = get_bst_from_list(lst)
        lst.remove(36)
        bst.bst_delete_r(36)
        lst.sort()
        self.assertEqual(lst, bst.bst_inorder_list_r())

    def test_bst_destroy_r(self):
        lst = [17,5,22,2,12,21,36,9,29,44,25,42]
        bst = get_bst_from_list(lst)
        bst.bst_destroy_r()
        self.assertEqual(0, bst.bst_get_size_r())

    def test_bst_destroy_nr(self):
        lst = [17,5,22,2,12,21,36,9,29,44,25,42]
        bst = get_bst_from_list(lst)
        bst.bst_destroy_nr()
        self.assertEqual(0, bst.bst_get_size_r())

    def test_bst_level_order_nr(self):
        lst = [50, 25, 75, 12, 40, 65, 95, 6, 20, 30, 45, 54, 70, 80, 100]
        bst = get_bst_from_list(lst)
        self.assertEqual(lst, bst.bst_levelorder_list_nr())

if __name__ == '__main__':
    print ("Running UT cases for binary_search_tree\n")
    unittest.main()





