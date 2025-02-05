
def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz', end="")
    elif i % 3 == 0:
        print('Fizz', end="")
    elif i % 5 == 0:
        print('Buzz', end="")
    else:
        print(i)
    stringified = str(i)
    if "3" in stringified:
        print('Fizz', end="")
    if "5" in stringified:
        print('Buzz', end="")

    print()

def main():
    for i in range(1, 101):
        fizzbuzz(i)

    fizzbuzz(53)
    fizzbuzz(35)

if __name__ == '__main__':
    main()

