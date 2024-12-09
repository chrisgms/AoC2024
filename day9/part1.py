file = "./example1.txt"
file = "./input1.txt"    

with open(file) as f:
    disk = list(map(int, f.read().strip()))

    diskIdx = 0
    checksum = 0
    lastFileIdx = len(disk) -1
    checkIdx = 0
    while diskIdx < len(disk):
        curr = disk[diskIdx]
        if curr == 0:
            diskIdx += 1
            continue

    
        if diskIdx % 2 == 0: #file
            upper = checkIdx + curr - 1
            mult = ((upper - checkIdx + 1) / 2) * (checkIdx + upper)
            checksum += mult * (diskIdx // 2)
            
            checkIdx += curr
            disk[diskIdx] = 0
            diskIdx += 1
        else:
            lastSpace = disk[lastFileIdx]

            if lastSpace == 0:
                diskIdx += 1
                continue

            lastId = (lastFileIdx // 2)
            availableSpace = min(curr, lastSpace)

            upper = checkIdx + availableSpace - 1
            mult = ((upper - checkIdx + 1) / 2) * (checkIdx + upper)
            checksum += mult * lastId

            checkIdx += availableSpace
            disk[diskIdx] -= availableSpace
            disk[lastFileIdx] -= availableSpace

            if disk[lastFileIdx] == 0:
                lastFileIdx -= 2
    
    print(int(checksum))
            
         
    
