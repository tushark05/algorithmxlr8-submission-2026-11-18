def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    # for i in range(0 , len(nums)):
    #     for j in range(i+1 , len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i ,j]

    hashmapp = {}

    for i in range(len(nums)):
        required = target-nums[i]

        if required in hashmapp:
            return [hashmapp[required],i]

        hashmapp[nums[i]] = i
    return -1

if __name__ == "__main__":
    print(main())
