with open("./input1.txt") as f:
    nums1, nums2 = list(map(list, zip(*[map(int,l.split()) for l in f.readlines()])))
   
    nums1.sort()
    nums2.sort()

    distance = 0
    for i1, i2 in zip(nums1, nums2):
        distance += abs(i1 - i2)
    
    print(distance)