import queue

class TreeNode:
    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChildren = left
        self.rightChildren = right
        self.parent = parent

    def hasLeftChildren(self):
        return self.leftChildren

    def hasRightChildren(self):
        return self.rightChildren

    def hasBothChildren(self):
        return self.leftChildren and self.rightChildren

    def isLeaf(self):
        return not (self.leftChildren or self.rightChildren)

    def isLeftChildren(self):
        # 有父节点 且 父节点的左孩子就是自己
        return self.parent and self.parent.leftChildren == self

    def isRightChildren(self):
        return self.parent and self.parent.rightChildren == self

    def isRoot(self):
        # 没有父节点
        return not self.parent


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, key, value):
        """
        1、插入的新元素key, 与当前的节点currentNode的值做比较
           key < currentNode.key 插入左子树
           key > currentnode.key 插入右子树
           key = currentNode.key 更新当前节点的值
        :param key:
        :return: 整课树
        """
        if self.root:
            self._add(key, value, self.root)
        else:
            self.root = TreeNode(key=key)
        self.size = self.size + 1
        return self.root

    def _add(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChildren():
                self._add(key, value, currentNode.leftChildren)
            else:
                currentNode.leftChildren = TreeNode(key, value, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChildren():
                self._add(key, value, currentNode.rightChildren)
            else:
                currentNode.rightChildren = TreeNode(key, value, parent=currentNode)
        elif key == currentNode.key:
            currentNode.value = value

    def search(self, key):
        """
        1、查找某个元素
           如果key < currentNode.key, 在左子树中查找
           如果key = currentNode.key, 返回value
           如果key > currentNode.key, 在右子树中查找
           没有找到，返回None

        :param key:
        :return: 返回元素对应的值value
        """
        if self.root:
            res = self._search(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _search(self, key, currentNode):
        if key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._search(key, currentNode.leftChildren)
        elif key > currentNode.key:
            return self._search(key, currentNode.rightChildren)
        else:
            return None

    def preOlder(self):
        if self.root:
            self._preOlder(self.root)

    def _preOlder(self, currentNode):
        if currentNode:
            print(currentNode.key)
            self._preOlder(currentNode.leftChildren)
            self._preOlder(currentNode.rightChildren)

    def levelOlder(self):
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.leftChildren:
                q.put(node.leftChildren)
            if node.rightChildren:
                q.put(node.rightChildren)

    def minNode(self):
        return self._minNode(self.root)

    def _minNode(self, currentNode):
        if currentNode.leftChildren is None:
            return currentNode
        return self._minNode(currentNode.leftChildren)

    def maxNode(self):
        return self._maxNode(self.root)

    def _maxNode(self, currentNode):
        if currentNode.rightChildren is None:
            return currentNode
        return self._maxNode(currentNode.rightChildren)

    def delete(self, key):
        pass

    def remove(self, currentNode):
        # 1、是叶子节点，没有子节点
        if currentNode.isLeaf():
            # 1.1 是叶子节点也要看当前节点是左孩子还是右孩子
            if currentNode.parent.leftChildren == currentNode:
                currentNode.parent.leftChildren = None
            else:
                currentNode.parent.rightChildren = None

        # 2、有两个子节点
        elif currentNode.hasBothChildren():
            # 2.1 这个currentNode是左节点
            if currentNode.isLeftChildren():
                # 2.1.1 在当前节点currentNode的右子树中找到最小的值
                min_node = self.minNode(currentNode.rightChildren)
                # 2.1.1.1 这个最小值有两种情况，一是叶子节点，或者是有一个右孩子
                # 2.1.1.1.1 是叶子节点
                if min_node.isLeaf():
                    # 将这个min_node 和 要删除的节点进行替换
                    pass
                # 2.1.1.1.2 有一个右孩子
                if min_node.hasRightChildren():
                    # 将min_node的右孩子放到min_node这个位置(min_node.parent.leftChildren), 然后将min_node
                    # 和 要删除的节点进行替换
                    pass
                pass
            # 2.2 这个currentNode是右节点
            elif currentNode.isRightChildren():
                # 2.2.1 在以当前节点currentNode为根的树中找到最小值
                # 2.2.1.1 这个最小值有两种情况，一是叶子节点，或者是有一个右孩子
                pass
            pass
        # 3、有一个子节点

        pass


if __name__ == "__main__":
    bst = BST()
    bst.add(17, 17)
    bst.add(5, 5)
    bst.add(35, 35)
    bst.add(2, 2)
    bst.add(11, 11)
    bst.add(29, 29)
    bst.add(38, 38)
    bst.add(9, 9)
    bst.add(16,16)
    bst.add(7, 7)
    bst.add(8, 8)

    # bst.preOlder()
    # bst.levelOlder()
    # print(bst.search(29))
