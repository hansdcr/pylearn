class Node:
    def __init__(self, data, next=None):
        """ Node 具有两个属性： 值(data), 指针(next)"""
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """ 初始化头节点 """
        self.head = None
        self.size = 0  # 用来记录链表的大小

    def add(self, data):
        """ 在头部添加节点 """
        node = Node(data)  # 创建一个新的节点
        node.next = self.head  # 将新节点的指针指向原来的头节点
        self.head = node  # 新的头节点现在变为这个新创建的节点

        self.size = self.size + 1

    def insert(self, index, data):
        """ 在指定位置插入节点 """
        # 找到这个位置
        if index < 0 or index > self.size:
            pass

        if index == 0:
            self.add(data)

        # 找到你要插入的元素的前一个元素
        prev = self.head  # 开始的时候prev和head指向同一个Node
        for i in range(index - 1):
            prev = prev.next  # 移动prev指针，知道要插入元素的前一个元素

        node = Node(data)
        node.next = prev.next  # 将新的node的指针指向原来的prev指针指向的node
        prev.next = node  # prev的指针指向变为当前的node

        self.size = self.size + 1

    def remove(self, index):
        # 找到这个位置
        if index < 0 or index > self.size:
            pass
        elif index == 0:
            self.head = self.head.next
            self.size = self.size - 1
        else:
            prev = self.head  # 开始的时候prev和head指向同一个Node
            for i in range(index - 1):
                prev = prev.next  # 移动prev指针，知道要插入元素的前一个元素
            prev.next = prev.next.next
            self.size = self.size - 1

    def print(self):
        cur = self.head
        while cur:
            print(f"->{cur.data}", end="")
            cur = cur.next


if __name__ == "__main__":
    L = LinkedList()
    L.add(None)
    L.add(5)
    L.add(4)
    L.add(3)
    L.add(2)
    L.add(1)
    #
    # L.insert(1, 666)
    #L.print()
    print('\n')
    # print('-----------')
    # L.remove(0)
    #
    # L.print()
    # print('\n')