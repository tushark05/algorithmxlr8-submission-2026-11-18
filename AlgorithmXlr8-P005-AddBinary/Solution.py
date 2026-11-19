# def main():
#     a = input().strip()
#     b = input().strip()

#     i = len(a) - 1
#     j = len(b) - 1
#     carry = 0
#     result = []

#     while i >= 0 or j >= 0 or carry:

#         # 1. Extract bit_a
#         if i>0:
#             bit_a = int(a[i])
#         else:
#             bit_a = 0

#         # 2. Extract bit_b
#         if j >0:
#             bit_b = int(b[j])
#         else:
#             bit_b = 0

#         # 3. Calculate total
#         total  = bit_a + bit_b + carry
#         # 4. Calculate resultbit
#         resultbit = total%2
#         # 5. Calculate carry
#         carry = total //2
#         # 6. Append resultbit
#         result.append(str(resultbit))
#         # 7. Decrease i and j
#         i-=1
#         j-=1

#     # 8. Reverse and join result
#     result.reverse()
#     # 9. Print final answer
#     answer = "".join(result)
#     print(answer)


def main():
    a = input().strip()
    b = input().strip()

    i = len(a) - 1
    j = len(b) - 1

    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:

        # Extract bits
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        # Calculate sum
        total = bit_a + bit_b + carry

        # Calculate result bit and carry
        result_bit = total % 2
        carry = total // 2

        # Store result
        result.append(str(result_bit))

        # Move pointers
        i -= 1
        j -= 1

    # Reverse and join
    answer = ''.join(result[::-1])

    print(answer)


if __name__ == "__main__":
    main()


