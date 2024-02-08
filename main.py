

class Switch:
    def __init__(self, num_ports):
        self.num_ports = num_ports
        self.current_match = list(range(num_ports))  # Initial state: input i connects to output i

    def get_neighbors(self, match):
        # Generating neighbors by swapping pairs of connections
        neighbors = []
        for i in range(self.num_ports):
            for j in range(i+1, self.num_ports):
                neighbor = match.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def compute_weight(self, match):
        # Placeholder for the actual weight computation logic
        return sum(match)  # Dummy computation

    def hamiltonian_walk(self, t):
        # Placeholder for the Hamiltonian walk computation
        return [list(range(self.num_ports))]  # Dummy walk

    def calculate_throughput(self, match):
        # Throughput is the number of outputs with matches
        return len(set(match))

    def run_time_slot(self, t, load):
        neighbors = self.get_neighbors(self.current_match)
        hamiltonian = self.hamiltonian_walk(t)
        all_matches = neighbors + hamiltonian

        # Compute weights for all matches (assuming the load is incorporated in the weight somehow)
        weighted_matches = [(match, self.compute_weight(match) + load) for match in all_matches]

        # Find the match with the maximum weight
        self.current_match = max(weighted_matches, key=lambda x: x[1])[0]
        
        # Calculate throughput for the current match
        throughput = self.calculate_throughput(self.current_match)
        return throughput

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