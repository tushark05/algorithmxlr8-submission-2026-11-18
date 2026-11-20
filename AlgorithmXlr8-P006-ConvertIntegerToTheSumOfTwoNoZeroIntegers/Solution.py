def main(n):
    def no_zero(x):
        return "0" not in str(x)

    for a in range(1, n):
        for b in range(1, n):
            if a + b == n and no_zero(a) and no_zero(b):
                return [a, b]
    return []


if __name__ == "__main__":
    n = int(input())
    print(main(n))
