fib = [0,1]
total = 0

while fib[-1] < 4000000:
    fib_next = fib[-1] + fib[-2]
    fib.append(fib_next)
    if fib[-1] %2 == 0:
        total += fib[-1]

print(fib)
print(total)
