class Node:
    def __init__(self, data):
        self.pref = None
        self.data = data
        self.nref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")
    
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def traverse_list(self):
        c = self.start_node
        print(c.data)
        c = c.nref
        while c.nref is not self.start_node.nref:
            print(c.data)
            c = c.nref
    
    def circularize(self):
        c = self.start_node
        while c.nref is not None:
            c = c.nref
        # print(c.data, 'is the final node')
        c.nref = self.start_node
        self.start_node.pref = c

    def calculate_length(self):
        c = self.start_node
        steps = 0
        while c is not self.start_node.pref:
            steps += 1
            c = c.nref
        steps += 1
        return steps
    
    def remove_item(self, item):
        if item == self.start_node:
            self.start_node = self.start_node.nref
        c = item
        c.pref.nref = c.nref
        c.nref.pref = c.pref

    