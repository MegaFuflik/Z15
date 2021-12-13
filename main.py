def max_pair(nums):    
    if (len(nums) == 0) or (len(nums) % 2 > 0):
        return 0
    max_pair = []
    i=0
    while i < len(nums):
        if i < len(nums):
            max_pair.append(nums[i] + nums[i+1])
            i = i + 1
        i = i + 1
    return(sorted(max_pair, reverse =True)[0])

if __name__ == "__main__":
    print(max_pair([]))
    print(max_pair([3,5,2]))
    print(max_pair([1,2,5,9]))