class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None


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
        cur = self.root
        self.root = cur.next
        return self.root  # num del elemento que quitaron
    

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
        cur = self.root
        while cur.next != None:
            if cur.next.next == None:
                d = cur.next
                cur.next = cur.next.next
                return d
            cur =cur.next
        
    

    def print_nodes(self):
        cur = self.root
        p = ""
        while cur is not None:
            p += str(cur.num) + ", "
            cur = cur.next
        print(p[:-2])


munch = Stack()

munch.push(3)
munch.push(6)
munch.push(9)
munch.push(12)

munch.print_nodes()
munch.pop()
munch.print_nodes()



        
