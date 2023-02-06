def main():
    x = int(input("what is x: "))
    y = int(input("what is y: "))
    added(x, y)
    divide(x, y)
    sub(x, y)
    multiply(x, y)
    modulus(x, y)
    power(x, y)


def added(x, y):
    print(x)
    print(y)
    print(x+y)


def divide(x, y):
    print(x)
    print(y)
    print(x/y)


def sub(x, y):
    print(x)
    print(y)
    print(x-y)


def multiply(x, y):
    print(x)
    print(y)
    print(x*y)


def modulus(x, y):
    print(x)
    print(y)
    print(x % y)


def power(x, y):
    print(x)
    print(y)
    print(x**y)


main()
