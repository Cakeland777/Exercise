https://www.acmicpc.net/problem/2747

def fibo(n):
    if n == 0:
        return 0
    elif n== (1 or 2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

N=int(input())
print(fibo(N))
