def main():
    coordinates = input().strip()
    # seprate out both charcters
    column = coordinates[0]
    row = coordinates[1]

    # convert to integer
    column_num = ord(column)-96
    row_num = int(row)

    # now check whether its black or white 
    if (column_num+row_num)%2 ==0:
        print("Black")
    else:
        print("White")

if __name__ == "__main__":
    main()