def best_sum(target_sum, nums, mem):
    if target_sum in mem:
        return mem[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    best_arr = None

    for num in nums:
        remainder = target_sum - num
        arr = best_sum(remainder, nums, mem)

        if arr != None:
            new_arr = [n for n in arr]
            new_arr.append(num)

            if best_arr == None or len(new_arr) < len(best_arr):
                best_arr = new_arr

    mem[target_sum] = best_arr

    return best_arr
    
def main():
    print(best_sum(7, [5, 3, 4, 7], dict())) #[7]
    print(best_sum(8, [2, 3, 5], dict())) #[5, 3]
    print(best_sum(8, [1, 4, 5], dict())) #[4, 4]
    print(best_sum(100, [1, 2, 5, 25], dict())) #[25, 25, 25, 25]

if __name__ == "__main__":
    main()
