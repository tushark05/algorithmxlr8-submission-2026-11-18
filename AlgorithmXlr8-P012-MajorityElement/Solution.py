def main():
    n = int(input())
    nums = list(map(int, input().split()))

    hashmapp = {}
    for i in range(len(nums)):
        if nums[i] in hashmapp:
            hashmapp[nums[i]] = hashmapp[nums[i]]+1
        else:
            hashmapp[nums[i]] = 1
        # next is that whether check majority is greate than N//2
        if hashmapp[nums[i]] > n//2:
            print(nums[i])
            return

if __name__ == "__main__":
    main()