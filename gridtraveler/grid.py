def grid_traveler(m, n, mem=dict()):
    key = stringify(m, n)
    if key in mem:
        return mem[key]

    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    mem[key] = grid_traveler(m-1, n, mem) + grid_traveler(m, n-1, mem) 

    return mem[key]

def stringify(m, n):
    return f"{m},{n}"

def main():
    print(grid_traveler(1,1))
    print(grid_traveler(2,3))
    print(grid_traveler(3,2))
    print(grid_traveler(3,3))
    print(grid_traveler(18,18))

if __name__ == "__main__":
    main()
