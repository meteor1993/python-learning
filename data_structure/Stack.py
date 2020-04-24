class Stack(object):

    def __init__(self):
        '''
        创建空列表实现栈
        '''
        self.__list = []

    def is_empty(self):
        '''
        判断是否为空
        :return:
        '''
        return self.__list == []

    def push(self,item):
        '''
        压栈，添加元素
        :param item:
        :return:
        '''
        self.__list.append(item)

    def pop(self):
        '''
        弹出栈，将元素取出
        :return:
        '''
        if self.is_empty():
            return
        else:
            return self.__list.pop()