def fibonacci_series(n):
    fib_sequence = [0, 1]  
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]


if __name__ == "__main__":
    n = int(input("Enter the number of terms you want in the Fibonacci series: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        print(fibonacci_series(n))