import random
from algorithms.binary_search_tree import binary_search_tree
from algorithms.redblack_tree import rb_tree


def generate_random_list(size, min, max):
    ret_set = set()
    random.seed()
    while len(ret_set) < size:
        ret_set.add(random.randint(min, max))
    ret = list(ret_set)
    random.shuffle(ret)
    return ret

def get_bst_from_list(bst_list):
    bst = binary_search_tree()
    for ele in bst_list:
        bst.bst_insert_r(ele)
    return  bst

def get_rbt_from_list(bst_list):
    rbt = rb_tree()
    for ele in bst_list:
        rbt.rbt_insert_nr(ele)
    return rbt

if __name__ == '__main__':
    pass
