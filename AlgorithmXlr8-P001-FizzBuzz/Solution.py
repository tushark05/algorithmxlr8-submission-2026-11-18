def main():
    n = int(input())
    otp = []
    for num in range(1 ,n+1) :
        if num% 3 == 0 and num%5== 0:
            otp.append("FizzBuzz")
        elif num % 3 ==0:
            otp.append("Fizz")
        elif num %5 ==0:
            otp.append("Buzz")
        else:
            otp.append(str(num))
    print(otp)
    # Write your solution here.
    # Print each answer on its own line: "FizzBuzz", "Fizz", "Buzz", or the number.
if __name__ == "__main__":
    main()