class Node:
    #creating a node with two attributes: 
    #the data-item and the next-node pointer
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    #creating a linked list with a pointer to the head node 
    def __init__(self):
        self.head = None

#Linked list operations

#Insertion
    #insert at the beginning
    def insertAtFirstIndex(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    #insert after a node
    def insertAfterNode(self, prev_node, new_data):

        if prev_node is None:
            print("Previous node not present")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #insert at the end
    def appendNode(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

#Deletion
    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        #find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        #if the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

#Traverse
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.item) + " ", end="")
            temp = temp.next

    def search(self, key):
        current = self.head

        while current is not None:
            if current.item == key:
                return True
            current = current.next

        return False

llist = LinkedList()

llist.appendNode(1)
llist.insertAtFirstIndex(2)
llist.insertAtFirstIndex(3)
llist.appendNode(4)
llist.insertAfterNode((llist.head.next).next, 5)

print('linked list:')
llist.printList()

print("\nAfter deleting an element:")
llist.deleteNode(3)
llist.printList()

print()
item_to_find = 3
if llist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")