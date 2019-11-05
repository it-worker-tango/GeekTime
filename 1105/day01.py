'''
题目链接：
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
'''
def Del(nums):
    for num_index in range(len(nums)-1, 0, -1):
        if nums[num_index] == nums[num_index-1]:
            nums.pop(num_index)
    return len(nums)

if __name__ == "__main__":
    test = [1, 1, 3, 1]
    a = Del(test)
    print(test)
    print(a)