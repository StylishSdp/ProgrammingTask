# #1.暴力搜索
def search(s1, s2):
    res = []
    if not s1 or not s2:
        res.append(-1)
        return res

    if len(s1) > len(s2):
        s1, s2 = s2, s1
        #s1是较短的

    start1, start2 = 0, 0
    end1, end2 = len(s1), len(s2)
    while start1 <= end1 and start2 < end2:
        if start1 == end1:
            res.append(start2 - start1)
            start2 = start2 - start1 + 1
            start1 = 0

        if start1 < end1 and start2 < end2:
            if s1[start1] == s2[start2]:
                start1 += 1
                start2 += 1
            else:
                start2 = start2 - start1 + 1
                start1 = 0
    if res:
        return res
    else:
        return [-1]


# #2.KMP算法
#
def prefix_table(s):
    prefix = [-1, 0]
    j = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == s[j]:
            j += 1
            prefix.append(j)
            i += 1
        else:
            prefix.append(0)
            j = 0
            i += 1
    return prefix

def KMP(s1, s2):

    res = []
    if not s1 or not s2:
        res.append(-1)
        return res

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    prefix = prefix_table(s1)
    i = 0
    j = 0
    res = []
    while j < len(s2):
        if i == len(s1) - 1 and s1[i] == s2[j]:
            res.append(j-i)
            i = prefix[i]

        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i = prefix[i]
            if i == -1:
                i += 1
                j += 1
    return res

s1 = 'ababcabaa'
s2 = 'abababcabaababcabaaa'
print(search(s1, s2))