# def search(nums):
#     res = 0
#     for i in range(len(nums)-1):
#         for j in range(i, len(nums)):
#             if nums[i] > nums[j]:
#                 res += 1
#     return res
#
# nums = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
# print(search(nums))


def MergeSort(nums):

    def sort_count(temp):
        if len(temp) == 1:
            return temp, 0
        else:
            n = len(temp) // 2
            temp1, count1 = sort_count(temp[0:n])
            temp2, count2 = sort_count(temp[n:])
            temp, count = merge(temp1, temp2, 0)
            return temp, count1+count2+count

    def merge(temp1, temp2, count):
        i = 0
        j = 0
        res = []
        while i < len(temp1) and j < len(temp2):
            if temp1[i] < temp2[j]:
                res.append(temp1[i])
                i += 1
            else:
                res.append(temp2[j])
                count += len(temp1) - i
                j += 1
        res += temp1[i:]
        res += temp2[j:]
        return res, count

    _, count = sort_count(nums)
    return nums, count

nums = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(MergeSort(nums)[1])

