def fib(n):
    if n <= 1: return n

    q = [[1, 1], [1, 0]] # [[fib(n+1), fib(n)], [fib(n), fib(n-1)]
    r = pow(q, n-1)
    return r[0][0]

def pow(m, n):
    if n == 0: return [[1, 0], [0, 1]] # identity
    if n == 1: return m

    a = pow(m, n//2)
    r = mult(a, a)
    if n & 1:
        r = mult(r, m)
    
    return r

def mult(a, b):
    r = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                r[i][j] += a[i][k] * b[k][j]
    return r

if __name__ == "__main__":
    for i in range(11):
        print(f'fib({i})', fib(i))
