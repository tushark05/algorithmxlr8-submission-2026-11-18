def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))
def solve(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j]!= 0:
            nums[i] = nums[j]
            i+=1
        # now we will fills all remaning position with zero
    while i<len(nums):
        nums[i] = 0
        i+=1
    return nums

if __name__ == "__main__":
    main()
