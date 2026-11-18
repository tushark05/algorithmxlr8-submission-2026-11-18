def main():
    num = input().strip()
    digits = list(num)
    for i in range(len(digits)):
        if digits[i] == '6' :
            digits[i] = '9'
            break
    result = "".join(digits)
    print(int(result))
      
if __name__ == "__main__":
    main()
