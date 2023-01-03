def fib(n, mem):
    if n <= 2: return 1
    if n in mem:
        return mem[n]

    mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]

def main():
    n = fib(100, dict())
    print(n)

if __name__ == "__main__":
    main()
