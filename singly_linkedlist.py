class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next  # Otherwise, remove the head by making the next node the new head

    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next:  # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None  # Remove the last node by setting the next pointer of the second-last node to None
    
    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 
    
    def add_middle(self, new_data):
        new_node = Node(new_data)

    # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # If new node should be inserted before head
        if new_data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            if new_data > temp.data and new_data <= temp.next.data:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        # If new_data is greater than all nodes (insert at end)
        temp.next = new_node
            # Make the new node the next node of the last node



if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()

    # Insert each letter at the beginning using the method we created
    llist.insertAtEnd('1') 
    llist.insertAtEnd('4') 
    llist.insertAtEnd('7')  
    llist.insertAtEnd('8')  
    llist.add_middle('5')
    print(llist.search("7"))
    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list
    llist.printList()       