class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        last = self.head
        while last.next :          
            last = last.next
        last.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, current.next)
            current = current.next
        print()

    def changeToArray(self):
        current = self.head
        arry = []
        while current:
            arry.append(current.data)
            current = current.next
        return arry

list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(4)


list2 = LinkedList()
# list2.append(1)
# list2.append(3)
# list2.append(4)

list2.append(0)

list1.display()
list2.display()

arry1 = list1.changeToArray()
arry2 = list2.changeToArray()
_join = sorted((arry1 + arry2))
print(arry1, arry2,)

list3 = LinkedList()
for x in _join:
    list3.append(x)

list3.display()