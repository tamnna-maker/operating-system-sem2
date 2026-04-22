# Banker's Algorithm Implementation
n = int(input("Enter number of processes: "))

# Number of resource types
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input().split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    row = list(map(int, input().split()))
    maximum.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# Calculate Need Matrix
need = []
for i in range(n):
    row = []
    for j in range(m):456
    
for i in range(n):
    print(need[i])

# Safety Algorithm
finish = [False] * n
safe_sequence = []
work = available.copy()

while len(safe_sequence) < n:
    found = False
    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i]
                    [j]

                safe_sequence.append(i)
                finish[i] = True
                found = True

    if not found:
        break

# Result
if len(safe_sequence) == n:
    print("\nSystem is in SAFE state")
    print("Safe sequence is:")
    for i in safe_sequence:
        print("P", i, end=" ")
else:
    print("\nSystem is NOT in safe state (Deadlock possible)")