def reverseWords(s):
    if not s:
        return s

    temp = []
    for i in s.split(' '):
        if i != '':
            temp.append(i)

    tmp = temp[::-1]
    return ' '.join(tmp)

s = "a good   example"
print(reverseWords(s))