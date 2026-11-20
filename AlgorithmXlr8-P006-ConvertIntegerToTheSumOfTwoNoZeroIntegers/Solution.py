# def main(n):
#     def no_zero(x):
#         return "0" not in str(x)

#     for a in range(1, n):
#         for b in range(1, n):
#             if a + b == n and no_zero(a) and no_zero(b):
#                 return [a, b]
#     return []

def get_no_zero_integers(n):
    def no_zero(x):
        while x > 0:
            if x % 10 == 0:
                return False
            x //= 10
        return True

    for a in range(1, n):
        if no_zero(a) and no_zero(n - a):
            return [a, n - a]
    return []

if __name__ == "__main__":
    n = int(input())
    print(get_no_zero_integers(n))
