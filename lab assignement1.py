# CPU Scheduling - FCFS and SJF 

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# -------- Input --------
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = input("Enter Process ID: ")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    processes.append(Process(pid, at, bt))


# -------- Display Input --------
print("\nProcess Table")
print("PID\tAT\tBT")

for p in processes:
    print(p.pid, "\t", p.at, "\t", p.bt)


# -------- FCFS Scheduling --------
print("\nFCFS Scheduling")

processes.sort(key=lambda x: x.at)

time = 0

for p in processes:

    if time < p.at:
        time = p.at

    time = time + p.bt
    p.ct = time
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt


print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)


avg_wt = sum(p.wt for p in processes) / n
avg_tat = sum(p.tat for p in processes) / n

print("Average Waiting Time =", avg_wt)
print("Average Turnaround Time =", avg_tat)


# -------- SJF Scheduling --------
print("\nSJF Scheduling")

completed = []
time = 0
remaining = processes.copy()

while remaining:

    available = [p for p in remaining if p.at <= time]

    if not available:
        time += 1
        continue

    p = min(available, key=lambda x: x.bt)

    time += p.bt
    p.ct = time
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt

    completed.append(p)
    remaining.remove(p)


print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in completed:
    print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)


avg_wt = sum(p.wt for p in completed) / n
avg_tat = sum(p.tat for p in completed) / n

print("Average Waiting Time =", avg_wt)
print("Average Turnaround Time =", avg_tat)