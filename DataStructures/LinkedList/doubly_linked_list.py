class Node:
    #creating a node with three attributes: 
    #the data-item, the next-node and previous node pointers
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoublyLinkedList:
    #creating a linked list with a pointer to the head node
    def __init__(self):
        self.head = None

#Linked list operations

#Insertion
    #insert at the beginning
    def insertAtFirstIndex(self, new_item):
        new_node = Node(new_item)
        
        self.head.prev = new_node
        new_node.next = self.head
        
        self.head = new_node

    #insert at an index
    def insertAtIndex(self, index, new_item):
        new_node = Node(new_item)

        if index == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return

        if self.head is None:
            print('List is Empty')
            return

        #find the node previous to the given index
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        #if the index is not present
        if temp is None or temp.next is None:
            print('Index not found')
            return

        next = temp.next

        next.prev = new_node
        temp.next = new_node

        new_node.prev = temp
        new_node.next = next

    #insert at the end
    def appendItem(self, new_item):
        new_node = Node(new_item)
        
        if self.head is None:
            self.head = new_node
            return

        last_item = self.head
        while last_item.next:
            last_item = last_item.next

        last_item.next = new_node
        new_node.prev = last_item

#Deletion
    def deleteNodeAt(self, index):

        if self.head is None:
            print('List is Empty')
            return

        if index == 0:
            self.head = temp.next
            self.head.prev = None
            temp = None
            return

        #find the node previous to the given index
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        #if the index is not present
        if temp is None or temp.next is None:
            print('Index not found')
            return

        next = temp.next.next

        temp.next = None

        temp.next = next
        if next is not None:
            next.prev = temp

#Traverse
    def printList(self):
        temp = self.head
        
        print('[',end='')
        while (temp.next):
            print(temp.item,end=",")
            temp = temp.next
        print(temp.item,end="]\n")

    def search(self, key):
        current = self.head

        while current is not None:
            if current.item == key:
                return True
            current = current.next

        return False

#Creating a doubly linked list object
dllist = DoublyLinkedList()

print('Insertion------------------------------------')

dllist.appendItem(10)
print('dllist.appendItem(10) => ',end='')
dllist.printList()

dllist.insertAtFirstIndex(20)
print('dllist.insertAtFirstIndex(20) => ',end='')
dllist.printList()

dllist.insertAtFirstIndex(30)
print('dllist.insertAtFirstIndex(30) => ',end='')
dllist.printList()

dllist.appendItem(40)
print('dllist.appendItem(40) => ',end='')
dllist.printList()

dllist.insertAtIndex(3, 50)
print('dllist.insertAtIndex(3, 50) => ',end='')
dllist.printList()

print('Deletion-----------------------------------')

dllist.deleteNodeAt(3)
print("dllist.deleteNodeAt(3) => ",end=' ')
dllist.printList()

print('Traversal-----------------------------------')
print("dllist.search(30) => ",end=' ')
item_to_find = 30
if dllist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")