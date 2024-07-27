class Process:
    def __init__(self, no, bt):
        self.no = no
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0

def read_process(i):
    print(f"\nProcess No: {i}")
    bt = int(input("Enter Burst Time: "))
    return Process(i, bt)

def main():
    processes = []
    avgtat = 0
    avgwt = 0
    current_time = 0
    
    print("<-- SJF Scheduling Algorithm Without Arrival Time (Non-Preemptive) -->")
    n = int(input("Enter Number of Processes: "))

    for i in range(n):
        processes.append(read_process(i + 1))

    # Sort processes based on Burst Time (BT)
    processes.sort(key=lambda p: p.bt)

    print("\nProcessNo\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        current_time += p.bt
        p.ct = current_time
        p.tat = p.ct
        avgtat += p.tat
        p.wt = p.tat - p.bt
        avgwt += p.wt
        print(f"P{p.no}\t\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}\t{p.wt}")

    avgtat /= n
    avgwt /= n
    print(f"\nAverage TurnAroundTime = {avgtat}")
    print(f"Average WaitingTime = {avgwt}")

if __name__ == "__main__":
    main()
