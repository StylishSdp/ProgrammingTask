def longestValidParentheses(s):
    if not s:
        return 0

    res = 0
    start = 0
    stack = []  #还是利用栈，栈里的元素时‘（’对应的index
    for i in range(len(s)):
        if s[i] == '(':    #是左括号，索引压栈
            stack.append(i)
        else:
            if len(stack) == 0:
                start = i + 1
            else:
                stack.pop()    #是右括号，且栈不为空的时候，栈顶出栈
                res = max(res, i - start + 1) if len(stack) == 0 else max(res, i -  stack[-1])
    return res

s = "()(()"
print(longestValidParentheses(s))