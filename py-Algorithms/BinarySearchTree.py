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
        return  self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent


class BTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BTreeNode(key, value)

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


if __name__ == "__main__":
    bt = BTree()
    bt.put(8, 1)
    bt.put(3, 1)
    bt.put(15, 1)
    bt.put(1, 1)
    bt.put(7, 1)
    bt.put(10, 1)
    bt.put(20, 1)
    bt.put(9, 1)
    bt.put(11, 1)
    bt.put(16, 1)
    bt.put(23, 1)

    bt.preOlder()
    # print('--------')
    # bt.midOlder()
    # print('--------')
    # bt.postOlder()
    #print('--------')
    #bt.preOlderNR()
    print('--------')
    bt.levelOlder()
    pass