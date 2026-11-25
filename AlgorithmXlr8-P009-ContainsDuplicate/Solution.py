# 

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(str(solve(nums)).lower())


# def solve(nums):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True

#     return False

# Second Approach

def solve(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
        else:
            return False

if __name__ == "__main__":
    main()