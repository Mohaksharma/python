### python 3.6.9 ###
class Stack(object):
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit
    
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])
    def push(self,data):
        if len(self.stack) >= self.limit:
            print("Stack Overflow")
        else:
            self.stack.append(data)
    def popl(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack) <= 0:
            print("Stack Underflow")
        else:
            return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
    def insertat(self,index,data):
        self.stack.insert(index,data)
    def validp(self,s: str) -> bool:
        self.stack = []
        flag = True
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                self.stack.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(self.stack) == 0:
                    flag = False
                    break
                else:
                    if s[i] == ')' and self.stack[-1] == '(':
                        self.stack.pop()
                    elif s[i] == ']' and self.stack[-1] == '[':
                        self.stack.pop()
                    elif s[i] == '}' and self.stack[-1] == '{':
                        self.stack.pop()
                    else:
                        flag = False
                        break
        return flag if len(self.stack) == 0 else False
        
    
#just uncomment theese lines below select them and then ctrl + k and then ctrl + u    
    
if __name__ == "__main__":
    mystack = Stack()
   # for i in range(10):
   #     mystack.push(i+1)
    #print(mystack)
   # print(mystack.isEmpty())
   # mystack.peek()
    #mystack.pop()
    #mystack.insertat(3,21)
   # print(mystack)
   # print(mystack.size())
    
    #s = "()]"
   # print(mystack.validp(s))
    
