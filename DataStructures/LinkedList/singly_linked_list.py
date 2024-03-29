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
    def insertAtFirstIndex(self, new_item):
        new_node = Node(new_item)

        new_node.next = self.head
        self.head = new_node

    #insert at an index
    def insertAtIndex(self, index, new_item):
        new_node = Node(new_item)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if self.head is None:
            print('List is Empty')
            return

        temp = self.head

        #find the node previous to the given index
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        #if the index is not present
        if temp is None or temp.next is None:
            print('Index not found')
            return

        next = temp.next

        temp.next = new_node

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

#Deletion
    def deleteNodeAt(self, index):

        if self.head is None:
            print('List is Empty')
            return

        temp = self.head

        if index == 0:
            self.head = temp.next
            temp = None
            return

        #find the node previous to the given index
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

#Creating a linked list object
llist = LinkedList()

print('Insertion------------------------------------')

llist.appendItem(10)
print('llist.appendItem(10) => ',end='')
llist.printList()

llist.insertAtFirstIndex(20)
print('llist.insertAtFirstIndex(20) => ',end='')
llist.printList()

llist.insertAtFirstIndex(30)
print('llist.insertAtFirstIndex(30) => ',end='')
llist.printList()

llist.appendItem(40)
print('llist.appendItem(40) => ',end='')
llist.printList()

llist.insertAtIndex(3, 50)
print('llist.insertAtIndex(3, 50) => ',end='')
llist.printList()

print('Deletion-----------------------------------')

llist.deleteNodeAt(3)
print("llist.deleteNodeAt(3) => ",end=' ')
llist.printList()

print('Traversal-----------------------------------')
print("llist.search(30) => ",end=' ')
item_to_find = 30
if llist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")