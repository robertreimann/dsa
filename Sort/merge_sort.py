import random


class MergeSort:
    def sort(nums):
        # left incluse, right excluse - [l, r)
        def merge_sort(l, r):
            # base case
            if r - l == 1: 
                return [nums[l]]
            
            mid = (l + r) // 2
            left_sub = merge_sort(l, mid)
            right_sub = merge_sort(mid, r)

            # put it back together in sorted order
            return MergeSort.merge(left_sub, right_sub)
        return merge_sort(0, len(nums))

    def merge(a, b):
        answer, p1, p2 = [], 0, 0
        while p1 < len(a) or p2 < len(b):
            if p1 < len(a) and p2 < len(b):
                if a[p1] < b[p2]:
                    answer.append(a[p1])
                    p1 += 1
                else:
                    answer.append(b[p2])
                    p2 += 1
            elif p1 < len(a):
                answer.append(a[p1])
                p1 += 1
            else:
                answer.append(b[p2])
                p2 += 1
        return answer
array = [30, 36, 16, 11, 22, 48, 32, 18, 3, 29, 2, 24, 33, 33, 15, 3, 0, 44, 8, 11, 31, 26, 49, 0, 28, 40, 22, 44, 28, 6, 47, 47, 28]
# [30, 36, 16, 11, 22, 48, 32, 18, 3, 29, 2, 24, 33, 33, 15, 3, 0, 44, 8, 11, 31, 26, 49, 0, 28, 40, 22, 44, 28, 6, 47, 47, 28]
print(array)
# [0, 0, 2, 3, 3, 6, 8, 11, 11, 15, 16, 18, 22, 22, 24, 26, 28, 28, 28, 29, 30, 31, 32, 33, 33, 36, 40, 44, 44, 47, 47, 48, 49]
print(MergeSort.sort(array))


