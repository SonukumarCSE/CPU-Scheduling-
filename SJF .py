class Process:
    def __init__(self, no, at, bt):
        self.no = no
        self.at = at
        self.bt = bt
        self.it = 0  # Idle Time or the time when the process starts executing
        self.ct = 0  # Completion Time
        self.tat = 0 # Turnaround Time
        self.wt = 0  # Waiting Time

def read_process(i):
    print(f"\nProcess No: {i}")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    return Process(i, at, bt)

def main():
    processes = []
    avgtat = 0
    avgwt = 0
    current_time = 0
    
    print("<-- SJF Scheduling Algorithm (Non-Preemptive) -->")
    n = int(input("Enter Number of Processes: "))

    for i in range(n):
        processes.append(read_process(i + 1))

    # Sort processes based on Arrival Time
    processes.sort(key=lambda p: p.at)

    # Find the first process to schedule based on burst time
    min_index = 0
    for j in range(1, n):
        if processes[j].at == processes[0].at and processes[j].bt < processes[min_index].bt:
            min_index = j
    processes[0], processes[min_index] = processes[min_index], processes[0]

    processes[0].it = processes[0].at
    processes[0].ct = processes[0].it + processes[0].bt

    # Schedule remaining processes
    for i in range(1, n):
        min_index = i
        for j in range(i + 1, n):
            if processes[j].at <= processes[i - 1].ct and processes[j].bt < processes[min_index].bt:
                min_index = j
        processes[i], processes[min_index] = processes[min_index], processes[i]

        if processes[i].at <= processes[i - 1].ct:
            processes[i].it = processes[i - 1].ct
        else:
            processes[i].it = processes[i].at
        processes[i].ct = processes[i].it + processes[i].bt

    print("\nProcess\t\tAT\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        p.tat = p.ct - p.at
        avgtat += p.tat
        p.wt = p.tat - p.bt
        avgwt += p.wt
        print(f"P{p.no}\t\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}\t{p.wt}")

    avgtat /= n
    avgwt /= n
    print(f"\nAverage TurnAroundTime = {avgtat}")
    print(f"Average WaitingTime = {avgwt}")

if __name__ == "__main__":
    main()
