# Disk Scheduling Algorithms (Beginner Friendly)

# FCFS Algorithm
def fcfs(requests, head):
    seek_time = 0
    print("\nFCFS Order:", end=" ")
    for r in requests:
        print(r, end=" ")
        seek_time += abs(head - r)
        head = r
    print("\nTotal Seek Time:", seek_time)


# SSTF Algorithm
def sstf(requests, head):
    seek_time = 0
    req = requests.copy()
    print("\nSSTF Order:", end=" ")

    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        print(nearest, end=" ")
        seek_time += abs(head - nearest)
        head = nearest
        req.remove(nearest)

    print("\nTotal Seek Time:", seek_time)


# SCAN Algorithm
def scan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    print("\nSCAN Order:", end=" ")

    for r in right:
        print(r, end=" ")
        seek_time += abs(head - r)
        head = r

    # go to end
    seek_time += abs(head - (disk_size - 1))
    head = disk_size - 1

    for r in left:
        print(r, end=" ")
        seek_time += abs(head - r)
        head = r

    print("\nTotal Seek Time:", seek_time)


# C-SCAN Algorithm
def cscan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    print("\nC-SCAN Order:", end=" ")

    for r in right:
        print(r, end=" ")
        seek_time += abs(head - r)
        head = r

    # jump to start
    seek_time += abs(head - (disk_size - 1))
    head = 0
    seek_time += disk_size - 1

    for r in left:
        print(r, end=" ")
        seek_time += abs(head - r)
        head = r

    print("\nTotal Seek Time:", seek_time)


# MAIN PROGRAM
requests = list(map(int, input("Enter disk requests (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

fcfs(requests, head)
sstf(requests, head)
scan(requests, head, disk_size)
cscan(requests, head, disk_size)
