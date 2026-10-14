def cal(x, y):
    sum = x + y
    sub = x - y
    mul = x * y
    div = x / y
    
    print("The sum of", x, "and", y, "is:", sum)
    print("The difference of", x, "and", y, "is:", sub)
    print("The product of", x, "and", y, "is:", mul)
    print("The quotient of", x, "and", y, "is:", round(div,2))

cal(8,11)