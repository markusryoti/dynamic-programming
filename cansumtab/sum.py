def can_sum(target_sum, nums):
    table = [False for x in range(target_sum + 1)]

    # seed value
    table[0] = True

    for curr in range(target_sum):
        if table[curr]:
            for n in nums:
                next_idx = curr + n

                if next_idx > target_sum:
                    continue

                table[next_idx] = True

    return table[-1]

def main():
    print(can_sum(7, [2, 3])) #false
    print(can_sum(7, [5, 4, 4, 7])) #true
    print(can_sum(7, [2, 4])) #false
    print(can_sum(8, [2, 3, 5])) # true
    print(can_sum(300, [7, 14])) # false

if __name__ == "__main__":
    main()
