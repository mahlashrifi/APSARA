

class Switch:
    def __init__(self, num_ports):
        self.num_ports = num_ports
        self.current_match = list(range(num_ports))  # Initial state: input i connects to output i





# Get input from the user
num_ports = int(input("Enter the number of ports for the switch: "))
num_time_slots = int(input("Enter the number of time slots to simulate: "))
load = int(input("Enter the load of the switch: "))

# Run the simulation
apsara_switch = Switch(num_ports)
# apsara_switch.run_simulation(num_time_slots, load)