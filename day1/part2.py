from collections import defaultdict

with open("./input1.txt") as f:
    nums1, nums2 = list(map(list, zip(*[map(int,l.split()) for l in f.readlines()])))
    
    counts = defaultdict(int)
    for n in nums2:
        counts[n] += 1

    similarity = 0
    for n in nums1:
        similarity += n * counts[n]

    print(similarity)