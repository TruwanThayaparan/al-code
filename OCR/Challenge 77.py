# Challenge 77 - Fib on a chi
# Created: 10/09/2026
# Last Updated: 10/09/2026

def fibonacci_loop(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        # e = a; a = b; b = e + b
        # print(a)
        fib.append(a)

    return fib
    
def fl_until_1000d():
    fib = []
    a, b = 0, 1
    while True:
        a, b = b, a + b
        fib.append(str(a))
        if len(str(a)) == 1000:
            x = len(fib)
            return a, x

fib4, x = fl_until_1000d()
print(fib4)
print(x)
