class TreeNode:
    def __init__(self):
        self._data = None
        self.left = None
        self.right = None
        
    def __del__(self):
        print("TreeNode of {} is deleted".format(self.data))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

class BinaryTree:
    def __init__(self):
        #멤버는 루트 노드를 가리키는 root 하나입니다.
        self.root = None

    #root 노드 반환
    def get_root(self):
        return self.root

    #root 노드 설정
    def set_root(self, r):
        self.root = r

    #새로운 노드를 만들어 반환합니다.
    def make_node(self):
        new_node = TreeNode()
        return new_node

    #노드의 데이터 반환
    def get_node_data(self, cur):
        return cur.data

    #노드의 데이터 설정
    def set_node_data(self, cur, data):
        cur.data = data

    #왼쪽 서브 트리 반환
    def get_left_sub_tree(self, cur):
        return cur.left

    #오른쪽 서브 트리 반환
    def get_right_sub_tree(self, cur):
        return cur.right

    #왼쪽 서브 트리를 만듭니다.
    def make_left_sub_tree(self, cur, left):
        cur.left = left

    #오른쪽 서브 트리를 만듭니다.
    def make_right_sub_tree(self, cur, right):
        cur.right = right

    #전위 순회로 트리를 순회 
    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    #중위 순회로 트리를 순회
    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)

    #후위 순회로 트리를 순회
    def postorder_traverse(self, cur, func):
        if not cur:
            return

        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)

if __name__ == "__main__":
    bt = BinaryTree()

    n1 = bt.make_node()
    bt.set_node_data(n1, 1)

    n2 = bt.make_node()
    bt.set_node_data(n2, 2)

    n3 = bt.make_node()
    bt.set_node_data(n3, 3)

    n4 = bt.make_node()
    bt.set_node_data(n4, 4)

    n5 = bt.make_node()
    bt.set_node_data(n5, 5)

    n6 = bt.make_node()
    bt.set_node_data(n6, 6)

    n7 = bt.make_node()
    bt.set_node_data(n7, 7)

    bt.set_root(n1)

    bt.make_left_sub_tree(n1, n2)
    bt.make_right_sub_tree(n1, n3)

    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)

    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)


    f = lambda x: print(x, end = '  ')
    
    bt.preorder_traverse(bt.get_root(), f)
    print("")

    bt.inorder_traverse(bt.get_root(), f)
    print("")

    bt.postorder_traverse(bt.get_root(), f)
    print("")

    '''
    #특정 위치에 노드 삽입
    n8 = bt.make_node()#1
    bt.set_node_data(n8, 8)

    bt.make_right_sub_tree(n1, n8)#2
    bt.make_right_sub_tree(n8, n3)#3

    bt.inorder_traverse(bt.get_root(), f)
    print("")
    '''
    '''
    #특정 위치의 노드 삭제
    bt.make_right_sub_tree(n6, n7)
    bt.make_right_sub_tree(n1, n6)
    #레퍼런트 카운트를 0으로 만들기 위해 n3를 삭제합니다.
    del n3

    bt.inorder_traverse(bt.get_root(), f)
    '''
    
    #특정 위치의 노드 삭제
    bt.make_right_sub_tree(n6, n7)
    bt.make_right_sub_tree(n1, n6)
    #레퍼런트 카운트를 0으로 만들기 위해 n3를 삭제합니다.
    del n3

    bt.inorder_traverse(bt.get_root(), f)
    
