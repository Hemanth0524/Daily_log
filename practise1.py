# even or odd, leap year, FizzBuzz

def even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


print(even_odd(9))
print(leap_year(2020))
print(fizz_buzz(15))