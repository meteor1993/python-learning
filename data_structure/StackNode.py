class Node(object):
    '''
    节点实现
    '''
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class Stack(object):
    def __init__(self):
        '''
        初始化链表头
        '''
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def push(self, item):
        '''
        压栈
        :param item:
        :return:
        '''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def pop(self):
        '''
        弹出栈
        :return:
        '''
        if self.is_empty():
            return
        else:
            p = self.__head
            self.__head = p.next
            return p.elem