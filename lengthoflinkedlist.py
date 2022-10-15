import singlylinkedlist
def checkl(a):
    count = 0
    temp = a.head
    while(temp != None):
        count += 1
        temp = temp.next
    return count
if __name__ == '__main__':
    a = singlylinkedlist.Linkedlist()
    for i in range(10):
        a.insertatbeg(i)
    a.printll()
    print()
    #print(a.getlength())
    #print('length: ',checkl(a))
