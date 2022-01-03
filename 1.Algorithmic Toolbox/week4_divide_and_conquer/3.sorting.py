# Uses python3
import sys
import random
# 
# def partition3(a, l, r):
#     #write your code here
#     x = a[l]
#     j = l
#     count = 1
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             if a[i] == x:
#                 count += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     a = list(filter(lambda y: y != x, a))
#     start_index = j-count+1
#     end_index = j
#     for i in range(start_index, start_index+count):
#         a.insert(i, x)
#     return a, start_index, end_index

def partition3(a, l, r):
    #write your code here
   x, j, t = a[l], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1   
   return j, t

# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # import time
    # n, *a = 5, [8,10,1,8,9,9,8,8,8,8,8,9,9,9,9,9,9,9,9,10,10,10,2,3,5,7,12,13]
    # # n, a = 5, [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
    # n = len(a)
    # while True:
    #     randomized_quick_sort(a, 0, n - 1)
    #     for x in a:
    #         print(x, end=' ')
    #     print('\n')
    #     time.sleep(0.5)
