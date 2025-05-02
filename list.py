class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtFirst(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def insertAtmid(self,data,x,temp):
        if not temp:
            return
        if x==1:
            temp2=Node(data)
            temp2.next=temp.next
            temp.next=temp2
            return
        self.insertAtmid(data,x-1,temp.next)            

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next            
        print(f"None")
if __name__=="__main__":

    llist=LinkedList()
    llist.insertAtFirst(10)
    # llist.insertAtFirst(20)
    # llist.insertAtFirst(30)
    llist.insertAtmid(101,2,llist.head)
    llist.print_list()

