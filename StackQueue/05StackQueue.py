class Node:
    def __init__(self, num):
        self.num = num
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def push(self, num):
        if self.root is None:
            self.root = Node(num)
        else:
            cur = self.root
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(num)

    # Quitar el primer elemento de la lista y regresar su valor
    def pop(self):
        print("pop Stack")
        return  # num del elemento que quitaron

    def print_nodes(self):
        cur = self.root
        p = ""
        while cur is not None:
            p += str(cur.num) + ", "
            cur = cur.next
        print(p[:-2])


class Queue:
    def __init__(self):
        self.root = None

    def push(self, num):
        if self.root is None:
            self.root = Node(num)
        else:
            cur = self.root
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(num)

    # Quitar el último elemento de la lista y regresar su valor
    def pop(self):
        print("pop Queue ")
        return  # num del elemento que quitaron

    def print_nodes(self):
        cur = self.root
        p = ""
        while cur is not None:
            p += str(cur.num) + ", "
            cur = cur.next
        print(p[:-2])
