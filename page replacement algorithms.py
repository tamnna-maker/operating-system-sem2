# Page Replacement Algorithms (Beginner Friendly)

# FIFO Algorithm
def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)   # remove oldest
                memory.append(page)
            faults += 1
    return faults


# LRU Algorithm
def lru(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
        else:
            memory.remove(page)
            memory.append(page)
    return faults


# Optimal Algorithm
def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                index = []

                for m in memory:
                    if m in future:
                        index.append(future.index(m))
                    else:
                        index.append(float('inf'))

                memory[index.index(max(index))] = pages[i]
            faults += 1
    return faults


# MRU Algorithm
def mru(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop()   # remove most recent
                memory.append(page)
            faults += 1
        else:
            memory.remove(page)
            memory.append(page)
    return faults


# MAIN PROGRAM
pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))

print("FIFO Page Faults:", fifo(pages, frames))
print("LRU Page Faults:", lru(pages, frames))
print("Optimal Page Faults:", optimal(pages, frames))
print("MRU Page Faults:", mru(pages, frames))