def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n]

n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is", fib(n))
