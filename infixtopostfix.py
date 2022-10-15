operator = set(['+','-','/','(',')','*','^'])
priority = {'+':1,'-':1,'*':2,'/':2,'^':3}

def getpostfix(exp):
    output = ''
    stack = []
    for ch in exp:
        if ch not in operator:
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[ch] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output

if __name__ == '__main__':
    exp = input('enter the expression :  ') 
    print('infix expression: ',exp)
    print('outfix expression: ',getpostfix(exp))
    
