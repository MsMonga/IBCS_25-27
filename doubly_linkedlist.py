class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null
        self.prev= None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        self.tail= None

    def traverse(self):
    # Traverse the doubly linked list and print its elements
        print("Start to finish")
        fwd = self.head
        while fwd:
      # Print current node's data
            print(fwd.data, end=" -> ")
        # Move to the next node
            fwd = fwd.next
        print("None")

        print("Finish to start")

        bkwd= self.tail
        while (bkwd):
            print(bkwd.data, end = "<-")
            bkwd=bkwd.prev
        print("none")

    def add(self,data):
        new_node = Node(data)
        ans = int(input("1 for insertion at beginning and 2 for insertion at the end"))
        if self.head is None: # if empty list
            self.head=new_node
            self.tail=new_node
            return
        if self.head and ans==1:  # node at the beginning
            new_node.next = self.head
            self.head.prev= new_node
            self.head = new_node
            return
        if self.tail and ans==2:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
            return

    def sorted_add(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if data<=self.head.data:
                new_node.next = self.head
                self.head.prev= new_node
                self.head = new_node
            elif data>=self.tail.data:
                new_node.prev=self.tail
                self.tail.next=new_node
                self.tail=new_node
            else:
                temp = self.head
                while temp:
                    if data>temp.data and data<=temp.next.data:
                        new_node.next=temp.next
                        temp.next.prev=new_node
                        temp.next=new_node
                        new_node.prev=temp
                        break
                    temp=temp.next



if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = DoublyLinkedList()
    llist.sorted_add(5)
    llist.sorted_add(3)
    llist.sorted_add(8)
    llist.sorted_add(6)
    llist.traverse()
