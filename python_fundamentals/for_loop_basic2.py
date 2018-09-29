# def biggieSize(arr):
#     for i in range (0, len(arr)):
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr
# print(biggieSize([3,-4,9,-2,6]))


# def positives(arr):
#     count = 0
#     for i in range (0, len(arr)):
#         if arr[i] > 0:
#             count += 1
#             arr[(len(arr)-1)] = count
#     return arr
# print(positives([3,2,-1,6,-4,9]))


# def sumTotal(arr):
#     sum = 0
#     for i in range (0, len(arr)):
#         sum += arr[i]
#     return sum
# print(sumTotal([5,3,1,9,12]))


# def averageNum(arr):
#     sum = 0
#     for i in range (0, len(arr)):
#         sum += arr[i]
#     avg = sum/len(arr)
#     return avg
# print(averageNum([7,2,4,9]))


# def lengthOf(arr):
#     count = 0
#     for i in range (0, len(arr)):
#         count += 1
#     return count
# print(lengthOf([5,2,4,1,6,7,9,8]))


# def Min(arr):
#     min = 0
#     for i in range (0, len(arr)):
#         if arr == " ":
#             return "False"
#         if arr[i] < min:
#             min = arr[i]
#     return min
# print(Min([6,2,3]))


# def Max(arr):
#     max = 0
#     for i in range (0, len(arr)):
#         if arr == " ":
#             return "False"
#         if arr[i] > max:
#             max = arr[i]
#         return max
# print(Max([5,4,18,9,14]))


def reverse(arr):
    for i in range (0, (len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp
    return arr
print(reverse([5,6,3,4]))