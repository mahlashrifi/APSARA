

class Switch:
    def __init__(self, num_ports):
        self.num_ports = num_ports
        self.current_match = list(range(num_ports))  # Initial state: input i connects to output i



    def run_simulation(self, num_time_slots, load):
        total_throughput = 0
        print("Time Slot | Current Match | Throughput")
        for t in range(num_time_slots):
            throughput = self.run_time_slot(t, load)
            total_throughput += throughput
            print(f"{t+1:9} | {str(self.current_match):14} | {throughput}")
            
        average_throughput = total_throughput / num_time_slots
        print(f"\nAverage Throughput over {num_time_slots} time slots: {average_throughput}")


# Get input from the user
num_ports = int(input("Enter the number of ports for the switch: "))
num_time_slots = int(input("Enter the number of time slots to simulate: "))
load = int(input("Enter the load of the switch: "))

# Run the simulation
apsara_switch = Switch(num_ports)
# apsara_switch.run_simulation(num_time_slots, load)