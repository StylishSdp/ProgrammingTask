def isValid(s):
    if not s:
        return True

    if len(s) % 2 != 0:   #通过一些明显的条件去掉一些False的例子
        return False
    if s[0] == ')' or s[0] == ']' or s[0] == '}':
        return False
    if s[-1] == '(' or s[-1] == '[' or s[-1] == '{':
        return False
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')' and stack[-1] == '(':   #匹配条件：当前为右括号，且栈顶为对应的左括号，才能出栈
            stack.pop()
        elif s[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif s[i] == '}' and stack[-1] == '{':
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False