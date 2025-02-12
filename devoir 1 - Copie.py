#Exercice 1
def fib(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
    return b
# Tests
print("Fibonacci de 75 est:", fib(75))
print("Fibonacci de 50 est:", fib(50))
print("Fibonacci de 100 est:", fib(100))