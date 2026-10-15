def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print(x, "is an even number")
    else:
        print(x, "is an odd number")


def is_even(num):
    return num % 2 == 0

main()

'''x = int(input("Enter a number: "))
if x % 2 == 0:
    print(x, "is an even number")
else:  
    print(x, "is an odd number")'''