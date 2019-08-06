def collatz(number):
    if number % 2 == 0:
        new_num = number // 2
        print(new_num)
        return new_num if new_num == 1 else collatz(new_num)
    else:
        new_num = 3 * number + 1
        print(new_num)
        return new_num if new_num == 1 else collatz(new_num)


def main():
    print("Enter a number")
    while True:
        number = input()

        try:
            collatz(int(number))
            break
        except ValueError:
            print("Please enter a number")
        

    
main()
