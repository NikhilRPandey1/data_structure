class Node:

    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:

    def __init__(self):
        self.head = None

    def __insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.pointer:
            itr = itr.pointer

        itr.pointer = Node(data, None)
        print("-----> add at end")

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data, self.head)
            self.head = new_node
        
        print("-----> add at beginning")

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.__insert_at_end(data)

    def delete_from_beginning(self):
        if self.head is not None:
            self.head = self.head.pointer
            print("----> delete from beginning")

    def delete_from_end(self):
        if self.head is not None:

            itr = self.head
            while itr.pointer.pointer is not None:
                itr = itr.pointer
            
            itr.pointer = None
            print("----> delete from end")

    def print(self):
        if self.head is None:
            print("List is empty.")
            return
        
        result: str = ""

        itr = self.head
        while itr:
            result += f"{itr.data} >>"
            itr = itr.pointer
        print(result)


ll: LinkedList = LinkedList()
ll.insert_values(["a", "b", "c", "d", "e"])
ll.print()
ll.insert_at_beginning("i")
ll.print()
ll.delete_from_beginning()
ll.print()
ll.delete_from_end()
ll.print()