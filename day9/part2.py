file = "./example1.txt"
file = "./input1.txt"

class MemoryNode:
    def __init__(self, isFile, space, id):
        self.isFile = isFile
        self.space = space
        self.id = id
        self.prev = None
        self.next = None
    
    def chain(self, indent = 0):
        curr = self
        while curr:
            print("\t"*indent, curr.id if curr.isFile else "_", curr.space)
            curr = curr.next
      

with open(file) as f:
    disk = list(map(int, f.read().strip()))
    
    head = MemoryNode(True, disk[0], 0)
    curr = head
    for idx, space in enumerate(disk[1:], start=1):
        if space:
            node = MemoryNode(idx % 2 == 0, space, idx // 2)
            curr.next = node
            node.prev = curr
            curr = node

    while curr:
        if not curr.isFile or curr.space == 0:
            curr = curr.prev
            continue

        spacePointer = head
        while spacePointer and spacePointer != curr:
            if spacePointer.space < curr.space: 
                spacePointer = spacePointer.next
                continue
            if not spacePointer.isFile:
                avail = min(spacePointer.space, curr.space)
                fileNode = MemoryNode(True, avail, curr.id)
                spaceNode = MemoryNode(False, avail, curr.id)

                spaceParent = spacePointer.prev
                spaceParent.next = fileNode
                fileNode.prev = spaceParent
                fileNode.next = spacePointer
                spacePointer.prev = fileNode

                fileChild = curr.next
                curr.next = spaceNode
                spaceNode.prev = curr
                spaceNode.next = fileChild
                if (fileChild): fileChild.prev = spaceNode
                
                spacePointer.space -= avail
                curr.space -= avail

                if spacePointer.space == 0:
                    spacePointer.prev.next = spacePointer.next
                    spacePointer.next.prev = spacePointer.prev
                if curr.space == 0:
                    curr.prev.next = curr.next
                    if (curr.next): curr.next.prev = curr.prev
                    break

            spacePointer = spacePointer.next

        curr = curr.prev
            
    checkIdx = 0
    checkSum = 0
    curr = head
    while curr:
        if curr.isFile:
            upper = checkIdx + curr.space - 1
            mult = ((upper - checkIdx + 1) / 2) * (checkIdx + upper)
            checkSum += mult * curr.id
        checkIdx += curr.space
        curr = curr.next
    
    print(int(checkSum))