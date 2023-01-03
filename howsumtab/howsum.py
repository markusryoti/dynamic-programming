def how_sum(target, nums):
    table = []

    for i in range(target + 1):
        table.append(None)

    table[0] = []

    for i in range(target + 1):
        if table[i] != None:
            for n in nums:
                next = i + n

                if next > target:
                    continue

                table[next] = [n for n in table[i]]
                table[next].append(n)

    return table[-1]

def main():
    print(how_sum(7, [2, 3])) # [3, 2, 2]
    print(how_sum(7, [5, 3, 4, 7])) # [4, 3]
    print(how_sum(7, [2, 4])) # null
    print(how_sum(8, [2, 3, 5])) # [2, 2, 2, 2]
    print(how_sum(300, [7, 14])) # null

if __name__ == "__main__":
    main()
