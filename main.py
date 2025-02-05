def fizzbuzz(i):
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
    for i in range(1, 101):
        fizzbuzz(i)

    fizzbuzz(53)
    fizzbuzz(35)

if __name__ == '__main__':
    main()

