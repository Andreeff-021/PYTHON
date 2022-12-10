with open('file_1.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

for i in range(1, len(nums)):
    if (nums[i] - nums[i - 1]) > 1:
        nums.insert(i, nums[i - 1] + 1)

print(nums)

with open('file_1.txt', 'w') as f:
    f.write(' '.join(list(map(str, nums))))