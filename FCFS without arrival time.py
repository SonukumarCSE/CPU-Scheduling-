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
    ct = 0
    
    print("<-- FCFS Scheduling Algorithm Without Arrival Time (Non-Preemptive) -->")
    n = int(input("Enter Number of Processes: "))

    for i in range(n):
        processes.append(read_process(i + 1))

    print("\nProcessNo\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        ct += p.bt
        p.ct = p.tat = ct
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
