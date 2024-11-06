def fibonacci_recursive_memo(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_recursive_memo(n - 1, memo) + fibonacci_recursive_memo(n - 2, memo)
    return memo[n]

# Example usage:
n = 10
print("Recursive Fibonacci with Memoization:", fibonacci_recursive_memo(n))

def fibonacci_iterative(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
n = 10
print("Iterative Fibonacci:", fibonacci_iterative(n))
