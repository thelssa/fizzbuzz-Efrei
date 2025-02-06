def fizzbuzz(i):
    """
    This function prints "Fizz" if i is divisible by 3, "Buzz" if i is divisible by 5, "FizzBuzz" if i is divisible by 3 and 5,
    :param i: int
    :return: None
    """
    result = ""
    if i % 3 == 0 and i % 5 == 0:
        result = "FizzBuzz"
    elif i % 3 == 0:
        result = "Fizz"
    elif i % 5 == 0:
        result = "Buzz"
    else:
        result = str(i)

    if "3" in str(i):
        result += "Fizz"
    if "5" in str(i):
        result += "Buzz"

    print(result)

def main():
    """
    main function to test fizzbuzz
    :return:
    """
    for i in range(1, 100):
        fizzbuzz(i)

    fizzbuzz(53)
    fizzbuzz(35)

if __name__ == '__main__':
    main()

