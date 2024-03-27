from itertools import permutations, islice
import random
import matplotlib.pyplot as plt


class Switch:
    def __init__(self, num_ports):
        self.num_ports = num_ports
        self.current_match = list(range(num_ports))  # Initial state: input i connects to output i
 
        self.input_buffers = []
        for i in range(num_ports):
            # Create a row for each input port which shows length of its virtuall queue 
            # (all virtuall queue are empty at first)
            buffer_row = [0 for _ in range(num_ports)]
            self.input_buffers.append(buffer_row)

    def get_neighbors(self, match):
        # Generating neighbors by swapping pairs of connections
        neighbors = []
        for i in range(self.num_ports):
            for j in range(i+1, self.num_ports):
                neighbor = match.copy()
                #swap values directly
                neighbor[i] , neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def compute_weight(self, match):
        weight = 0
        for i, output in enumerate(match):
            if self.input_buffers[i][output] > 0:
                weight+=1
        return weight

    def hamiltonian_walk(self, t):
        perm_iter = permutations(range(self.num_ports))
        selected_perm = next(islice(perm_iter, t, None), None)
        return list(selected_perm) if selected_perm else list(range(self.num_ports))

    def calculate_throughput(self, match):
        throughput = 0
        for i, output in enumerate(match):
            if self.input_buffers[i][output] > 0:  # Check if there is at least one packet to send
                throughput += 1
        return throughput

    def run_time_slot(self, t):
        # Get all neighbor matchings
        neighbors = self.get_neighbors(self.current_match)
        
        # Start with the current match as the best match
        max_weight = self.compute_weight(self.current_match)
        best_match = self.current_match
        
        # Check all neighbor matchings to find the best one
        for neighbor in neighbors:
            weight = self.compute_weight(neighbor) 
            if weight > max_weight:
                max_weight = weight
                best_match = neighbor
        
        # Compute the Hamiltonian walk and its weight
        hamiltonian = self.hamiltonian_walk(t)
        hamiltonian_weight = self.compute_weight(hamiltonian)
        
        # Check if the Hamiltonian walk is better than the current best
        if hamiltonian_weight > max_weight:
            best_match = hamiltonian
        
        # Set the best matching as the current match
        self.current_match = best_match
        
        # Calculate throughput for the current match
        throughput = self.calculate_throughput(self.current_match)
        return throughput
    
    def update_input_buffers(self):
        for in_port in range(self.num_ports):  
            self.input_buffers[in_port][random.randint(0, self.num_ports-1)] += 1

    def process_current_match(self):
        # Process the matching to reduce the number of packets in the queues
        for in_port, out_port in enumerate(self.current_match):
            if self.input_buffers[in_port][out_port] > 0:
                self.input_buffers[in_port][out_port] -= 1     

    def run_simulation(self, num_time_slots):
        total_throughput = 0
        print("Time Slot | Current Match | Throughput")
        for t in range(num_time_slots):
            self.update_input_buffers()
            throughput = self.run_time_slot(t)/(self.num_ports)
            total_throughput += throughput
            print(f"{t+1:9} | {str(self.current_match):14} | {throughput}")
            self.process_current_match()

        average_throughput = total_throughput / num_time_slots
        print(f"\nAverage Throughput over {num_time_slots} time slots: {average_throughput}")
        return average_throughput


def plot_throughput_vs_ports(num_time_slots):
    port_numbers = [4, 5, 6, 7, 8]
    average_throughputs = []  #

    for num_ports in port_numbers:
        switch = Switch(num_ports)  
        average_throughputs.append(switch.run_simulation(num_time_slots))

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(port_numbers, average_throughputs, marker='o', linestyle='-', color='b')
    plt.title('Average Throughput vs. Number of Ports')
    plt.xlabel('Number of Ports')
    plt.ylabel('Average Throughput')
    plt.xticks(port_numbers)
    plt.grid(True)
    plt.show()

def run():

    num_ports = int(input("Enter the number of ports for the switch: "))
    num_time_slots = int(input("Enter the number of time slots to simulate: "))

    apsara_switch = Switch(num_ports)
    apsara_switch.run_simulation(num_time_slots)


#To run for specific number of time-slots and ports
run()
# depicting effect of number port number on throughput for specific number of time-slots 
plot_throughput_vs_ports(31035)
