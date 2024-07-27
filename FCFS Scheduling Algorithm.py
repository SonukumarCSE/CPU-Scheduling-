class Process:
    def __init__(self, no, at, bt):
        self.no = no
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0

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
    
    print("<-- FCFS Scheduling Algorithm (Non-Preemptive) -->")
    n = int(input("Enter Number of Processes: "))

    for i in range(n):
        processes.append(read_process(i + 1))
    
    # Sort processes based on Arrival Time
    processes.sort(key=lambda p: p.at)

    print("\nProcessNo\tAT\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        if current_time < p.at:
            current_time = p.at  # Adjust current time to the arrival time of the next process
        current_time += p.bt
        p.ct = current_time
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
