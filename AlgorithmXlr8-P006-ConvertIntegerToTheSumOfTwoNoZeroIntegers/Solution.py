import sys
def main(n):
    a = 1
    for a in range(1 , n):
        b = n - a
        if "0" not in str(a) and "0" not in str(b):
            return [a,b]
            
if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    print(main(n))