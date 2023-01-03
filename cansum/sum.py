def can_sum(target_sum, nums, mem):
    if target_sum in mem:
        return mem[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in nums:
        remainder = target_sum - num 

        if can_sum(remainder, nums, mem):
            mem[target_sum] = True
            return True

    mem[target_sum] = False
    return False
    
def main():
    print(can_sum(7, [2, 3], dict())) #true
    print(can_sum(7, [5, 3, 4, 7], dict())) #true
    print(can_sum(7, [2, 4], dict())) #false
    print(can_sum(8, [2, 3, 5], dict())) #true
    print(can_sum(300, [7, 14], dict())) #true

if __name__ == "__main__":
    main()
