

def evalRPN(tokens):
    f1 = lambda a, b: a+b
    f2 = lambda a, b: a - b
    f3 = lambda a, b: a * b
    f4 = lambda a, b: int(a/b)
    hashmap = {'+':f1, '-':f2, '*':f3, '/':f4}

    stack = []
    for i in tokens:
        if i in hashmap.keys():   #将运算符之前的两个数字压栈
            #遍历到字符时，将栈中的两个数字弹出来
            b = stack.pop()
            a = stack.pop()
            stack.append(hashmap[i](a,b))
        else:
            stack.append(int(i))

    return stack[-1]

s = ["2","1","+","3","*"]
print(evalRPN(s))