class Node:
    def __init__(self,data):
        self.data= data
        self.prev= None   #address of the previous node
        self.next= None   #address of the next node
        
class DoublyLL:
    def __init__(self):
        self.head= None
        
    def searching(self, data):
        t= 0
        temp= self.head
        #traversing the list through temp
        while temp:
            if temp.data== data:
                t= 1
                break #break the loop when the element is found
            temp= temp.next
        if t==1:
            print(f"Element {data} found")
        else:
            print(f"Element {data} not found")
            
    def display(self):
        if(self.head== None):
            print("List is empty")
        else:
            temp= self.head
            while temp:
                print(temp.data, "-->", end= " ")
                temp= temp.next
                
l= DoublyLL()
n= Node(10)
l.head= n
n1= Node(20)
n.next= n1
n2= Node(30)
n2.prev= n1
n1.next= n2
l.display()
print(end= "\n")
l.searching(30)
        