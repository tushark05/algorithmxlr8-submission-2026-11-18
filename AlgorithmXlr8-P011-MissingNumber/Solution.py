def main():
    n = int(input())
    nums = list(map(int, input().split()))
    # print(solve(nums))

    n = len(nums)
    for i in range(0 , n+1):
        if i not in nums:
            print(i)
            return 

# def solve(nums):
#     n = len(nums)
#     for i in range(0 , n ):
#         if nums[i] not in num:
#             return nums[i]
        

if __name__ == "__main__":
    main()