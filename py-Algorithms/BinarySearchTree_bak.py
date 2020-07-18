from queue import Queue


class BTreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.isleftchild = False
        self.isrightchild = False
        self.nodeCount = 1

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChild(self):
        return  self.leftChild and self.rightChild


class BTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BTreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = BTreeNode(key, value, parent=currentNode)
        elif key == currentNode.key:
            currentNode.value = value
        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = BTreeNode(key, value, parent=currentNode)

    # 前序遍历
    def preOlder(self):
        self._preOlder(self.root)

    def _preOlder(self, treeNode):
        if treeNode:
            print(treeNode.key)
            self._preOlder(treeNode.leftChild)
            self._preOlder(treeNode.rightChild)

    # 中序遍历
    def midOlder(self):
        self._midOlder(self.root)

    def _midOlder(self, treeNode):
        if treeNode:
            self._midOlder(treeNode.leftChild)
            print(treeNode.key)
            self._midOlder(treeNode.rightChild)

    # 后序遍历
    def postOlder(self):
        self._postOlder(self.root)

    def _postOlder(self, treeNode):
        if treeNode:
            self._postOlder(treeNode.leftChild)
            self._postOlder(treeNode.rightChild)
            print(treeNode.key)

    # 非递归的前序遍历
    def preOlderNR(self):
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            print(node.key)
            if node.leftChild is not None:
                stack.append(node.rightChild)
            if node.rightChild is not None:
                stack.append(node.leftChild)

    # 层级遍历
    def levelOlder(self):
        q = Queue()
        q.put(self.root)
        while q.qsize() > 0:
            treeNode = q.get()
            print(treeNode.key)
            if treeNode.leftChild:
                q.put(treeNode.leftChild)
            if treeNode.rightChild:
                q.put(treeNode.rightChild)

    # 最小值
    def minimum(self):
        node = self.root
        while node.leftChild:
            node = node.leftChild
        return node

    # 二分搜索树查找最小值
    def minimum2(self):
        return self._minimum2(self.root)

    def _minimum2(self, node):
        if node.leftChild is None:
            return node
        return self._minimum2(node.leftChild)

    # 二分搜索树查找最大值
    def maximum(self):
        return self._maximum(self.root)

    def _maximum(self, node):
        if node.rightChild is None:
            return node
        return self._maximum(node.rightChild)

    # def removeMin(self):
    #     min_node = self.minimum()
    #     self._removeMin(min_node)
    #     return min_node

    # def _removeMin(self, node):
    #     if node.leftChild is None:
    #         right_child = node.rightChild
    #         node.rightChild = None
    #         return right_child
    #     node.leftChild = self._removeMin(node.leftChild)
    #     return node
    #
    # def removeMax(self):
    #     max_node = self._maximum()
    #     self._removeMax(max_node)
    #     return max_node
    #
    # def _removeMax(self, node):
    #     if node.rightChild is None:
    #         left_child = node.leftChild
    #         node.leftChild = None
    #         return left_child
    #     node_rightChild = self._removeMax(node.rightChild)
    #    return  node

    # 删除二叉树中任意节点

    # 查找任意值，返回值对应的节点
    def search(self, key):
        pass

    def remove(self, currentNode):
        # 是叶子节点
        if currentNode.isLeaf():
            if currentNode.parent.leftChild == currentNode:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # 有两个子节点
        elif currentNode.hasBothChild():
            # 找到右子树中最小的值，替换当前节点
            if currentNode.hasRightChild():
                rightChild = currentNode.rightChild
                # 在右子树中找到最小的节点
                min_node = self._minimum2(rightChild)
                # 替换当前节点

            if currentNode.hasLeftChild():
                rightChild = currentNode.rightChild
                min_node = self._minimum2(rightChild)
                currentNode.rightChild.parent = min_node

        # # 有一个子节点
        # elif currentNode.hasAnyChild():
        #     if currentNode.isLeftChild():
        #         if currentNode.hasLeftChild():
        #             currentNode.parent.leftChild = currentNode.leftChild
        #             currentNode.leftChild = None
        #         elif currentNode.hasRightChild():
        #             currentNode.parent.leftChild = currentNode.rightChild
        #             currentNode.rightChild = None
        #     if currentNode.isRightChild():
        #         if currentNode.hasLeftChild():
        #             currentNode.parent.rightChild = currentNode.leftChild
        #             currentNode.leftChild = None
        #         elif currentNode.hasRightChild():
        #             currentNode.parent.rightChild = currentNode.rightChild
        #             currentNode.rightChild = None


if __name__ == "__main__":
    bt = BTree()
    bt.put(8, 1)
    bt.put(4, 1)
    bt.put(15, 1)
    bt.put(2, 1)
    bt.put(6, 1)
    bt.put(10, 1)
    bt.put(20, 1)
    bt.put(1, 1)
    bt.put(3, 1)
    bt.put(5, 1)
    bt.put(7, 1)
    bt.put(9, 1)
    bt.put(11, 1)
    bt.put(16, 1)
    bt.put(23, 1)

    bt.preOlder()
    # print('--------')
    # bt.midOlder()
    # print('--------')
    # bt.postOlder()
    # print('--------')
    # bt.preOlderNR()
    print('--------')
    # bt.levelOlder()


    #bt.remove()

