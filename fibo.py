def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
n = 10
print("Iterative Fibonacci:", fibonacci_iterative(n))


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = 10
print("Recursive Fibonacci:", fibonacci_recursive(n))
