# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0

# a, b, c = int(input('Введите число A: ')), int(input('Введите число B: ')), int(input('Введите число C: '))
str1 = '- 4 * x^2 + 4 * x + 1 = 0'
nums = str1.split()

nums1 = []
for i in nums:
    if i.isdigit() or i == '-':
        nums1.append(i)
print(nums1)

# i = 0
# while nums1.count('-') != 0:
#     if nums[i] == '-':
#         nums1[i] += nums1[i + 1]
#         nums1.pop(i + 1)
#         i = 0
#     i += 1
#     print(nums1)

# i = 0
# while len(nums) > 0:
#     if not nums[i].isdigit():
#         if nums[i] != '-':
#             nums.remove(nums[i])
#             i -= 1
#     else:
#         nums1.append(nums[i])
#         # nums.remove(nums[i])
#     i += 1
#
# print(nums1)



# d = b ** 2 - 4 * a * c
# if d < 0:
#     print('no roots')
# elif d == 0:
#     print(round(b / (2 * a), 2))
# else:
#     print(round((- b + (d ** 0.5)) / (2 * a), 2))
#     print(round((- b - (d ** 0.5)) / (2 * a), 2))