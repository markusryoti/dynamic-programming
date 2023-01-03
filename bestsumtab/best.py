def best_sum(target_sum, nums):
    table = [None for x in range(target_sum + 1)]

    table[0] = []

    for curr in range(target_sum):
        if table[curr] != None:
            for n in nums:
                next_idx = curr + n

                if next_idx > target_sum:
                    continue
                
                if table[next_idx] != None:
                    if len(table[next_idx]) < len(table[curr]) + 1:
                        continue
                
                table[next_idx] = [n for n in table[curr]] + [n]

    return table[-1]

def main():
    print(best_sum(7, [5, 3, 4, 7])) # [7]
    print(best_sum(8, [2, 3, 5])) # [3, 5]
    print(best_sum(8, [1, 4, 5])) # [4, 4]
    print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]

if __name__ == "__main__":
    main()
