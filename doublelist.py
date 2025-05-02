class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtFirst(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            return
        node.next=self.head
        self.head.prev=node
        self.head=node

    def insertAtLast(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            return
        temp=self.head
        while temp:
            if not temp.next:
                break
            temp=temp.next
        temp.next=node
        node.prev=temp    

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")         


if __name__=="__main__":
    dll=DoubleLinkedList()
    dll.insertAtFirst(10)
    dll.insertAtFirst(20)
    dll.insertAtLast(40)
    dll.insertAtFirst(50)
    dll.insertAtLast(101)
    dll.print_list()