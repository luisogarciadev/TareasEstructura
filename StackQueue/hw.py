class Node:
    def __init__(self,num):
        self.num = num
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.root = None

    def add_node(self,num):
            if self.root == None:
                self.root = Node (num)
            elif self.root != None:
                cur = self.root
                while (cur.next != None):
                    cur = cur.next
                cur.next = Node(num)
            else:
                cur = self.root
                while (cur.next != None):
                    cur = cur.next.prev
                cur.next.prev = Node(num)

    def print_nodes(self):
        cur = self.root
        while (cur != None):
            print(cur.num)
            cur = cur.next

    def search(self,num):
        cur = self.root
        while(cur != None):
            if cur.num == num:
                print("Se encontro el numero!".format(num))
                return True
            cur = cur.next
        print("No se encontro el numero {} en la lista".format(num))
        return False

    def remove_node(self,num):
        if self.root == None:
            print("Lista vacia")
        elif self.root.num == num:
            self.root = self.root.next
            print("Numero {} borrado".format(num))
            return True
        else:
            cur = self.root
            while(cur.next != None):
                if cur.next.num == num:
                    cur.next =  cur.next.next
                    print("Numero {} borrado".format(num))
                    return True
                elif cur.next.num != num:
                 cur.next = cur.next.prev
                 print("Numero {} borrado".format(num))
                 return True
            cur = cur.next
            print("Numero {} no encontrado".format(num))
            return False

class Stack:
    def __init__(self):
        self.root = None

    def push(self,num):
        if self.root is None:
            self.root = Node(num)
        else:
            cur = self.root
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(num)

     def pop(self):
         cur = self.root
         print("Numero {} que se borro".format(cur.num))
         self.root = cur.next

    def print_nodes(self):
         cur = self.root
         p =""
         while cur is not None:
             p+= str(cur.num) + ","
        print(p[:-2])

class Queue:
    def __init__(self):
        self.root = None

    def push(self,num):
        if self.root is None:
            self.root = Node(num)
        else:
            cur = self.root
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(num)

    def pop(self):
        cur = cur.next.next
        print("Numero {} se borro".format(cur.next.next.num))

    def print_nodes(self):
        cur = self.root
        p = ""
        while cur is not None:
            p += str(cur.num) + ","
            cur = cur.next
        print(p[:-2])





ll = LinkedList()
ll.add_node(3)
ll.add_node(6)
ll.add_node(8)
ll.add_node(4)
ll.print_nodes()
ll.remove_node(4)
ll.print_nodes()