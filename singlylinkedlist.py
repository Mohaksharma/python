class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
    def setdata(self,data):
        self.data = data
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next = next
    def getnext(self):
        return self.next

class Linkedlist(object):
    #defining the head of the linkedlist
    def __init__(self):
        self.head = None
    def insertatbeg(self,data):
        node = Node(data,self.head)
        self.head = node
    def printll(self):
        if self.head is None:
            print('LL is empty')
            return
        it = self.head
        llstr = ''
        while(it):
            llstr += str(it.data) + ' '
            it = it.next
        print(llstr)
    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        it = self.head
        while it.next:
            it = it.next
        it.next = Node(data,None)
    def insertvalues(self,data_list):
        self.head = None
        for data in data_list:
            self.insertatend(data)
    def getlength(self):
        count = 0
        it = self.head
        while it:
            count += 1
            it = it.next
        return count
    def insertbet(self,prevnode,data):
        if prevnode is None:
            print('previous node should have a next node')
        else:
            newnode = Node(data)
            newnode.next = prevnode.next
            prevnode.next = newnode
    def delete(self,data):
        temp = self.head
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            else:
                while(temp.next!=None):
                    if temp.data == data:
                        break
                    prev = temp
                    temp = temp.next
                #node not found
                if temp == None:
                    return
                prev.next = temp.next
                return
    def search(self,node,data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getnext(),data)

if __name__ == '__main__':
    ll = Linkedlist()
    ll.head = Node(1)
    node2 = Node(2)
    ll.head.setnext(node2)
    node3 = Node(3)
    node2.setnext(node3)
    ll.insertatbeg(4)              # node4's next --> head-node --> node2 --> node3
    ll.insertbet(node2, 5)       # node2's next --> node5
    ll.insertatend(6)
    ll.printll()
    print(ll.search(ll.head, 1))
