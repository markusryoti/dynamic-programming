def how_sum(target_sum, nums, mem):
    if target_sum in mem:
        return mem[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in nums:
        remainder = target_sum - num
        arr = how_sum(remainder, nums, mem)

        if arr != None:
            arr.append(num)
            mem[target_sum] = arr
            return arr

    mem[target_sum] = None
    return None
    
def main():
    print(how_sum(7, [2, 3], dict())) #[3,2,2]
    print(how_sum(7, [5, 3, 4, 7], dict())) #[4,3]
    print(how_sum(7, [2, 4], dict())) #None
    print(how_sum(8, [2, 3, 5], dict())) #[2,2,2,2]
    print(how_sum(300, [7, 14], dict())) #None

if __name__ == "__main__":
    main()
