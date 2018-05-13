# BST
from binary_tree import *

class BST(BinaryTree):
    def insert(self, data):
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()

        # bst is empty
        if not cur: #cur이 없을 때
            self.set_root(new_node)
            return

        while True:
            if data < self.get_node_data(cur): #data가 cur보다 적다면
                if self.get_left_sub_tree(cur):
                    cur = self.get_left_sub_tree(cur)
                else:
                    self.make_left_sub_tree(cur, new_node)
                    break
            else:
                if self.get_right_sub_tree(cur):
                    cur = self.get_right_sub_tree(cur)
                else:
                    self.make_right_sub_tree(cur, new_node)
                    break


    def search(self, target):
        cur = self.get_root()

        while cur: #cur이 있다면
            if target == self.get_node_data(cur):
                return cur
            elif target < self.getnode_data(cur):
                cur = self.get_left_sub_tree(cur)
            else:
                cur = self.get_right_sub_tree(cur)

        return cur


    def remove(self, target):
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            if not del_node:
                return None

            if target == self.get_node_data(del_node):
                break
            elif target < self.get_node_data(del_node):
                del_parent = del_node
                del_node = self.get_left_sub_tree(del_node)
            else:
                del_parent = del_node
                del_node = self.get_right_sub_tree(del_node)

        #리프나 자식 하나나 자식 둘이나










