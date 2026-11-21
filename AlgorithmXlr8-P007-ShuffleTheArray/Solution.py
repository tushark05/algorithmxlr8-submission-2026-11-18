def main(n , nums):

# """
# 1.Take the input array nums.
# 2.Initialize an empty array called result.
# 3Initialize the first pointer at index 0.
# 4.Initialize the second pointer at index n.
# 5.Run a loop n times.
# 6.Append the element at the first pointer.
# 7.Append the element at the second pointer.
# 7.Increment both pointers.
# 7.Return the result.
# """
    result = []
    i = 0
    j = n
    for _ in range(n):
        result.append(nums[i])
        result.append(nums[j])

        i+=1
        j+=1
    return result

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(main(n ,nums))