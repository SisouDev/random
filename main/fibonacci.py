def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == '__main__':
    a = int(input("Digite um número: "))
    print(Fibonacci(a))
    print(Fibonacci(a+1))
    print(Fibonacci(a+2))
    print(Fibonacci(a+3))
