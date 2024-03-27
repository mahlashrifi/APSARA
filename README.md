# ASPARA 
This is second practical homework of netwrok device course at AUT in fall 2023

The ASPARA algorithm implemented in this project is based on the approach outlined in 'High Performance Routers and Switches,' authored by Liu Bin and Chao Jonathan R.

You can find implementation details [here](https://github.com/mahlashrifi/APSARA/blob/master/refrence.jpeg).

## Introduction
Network switches play a vital role in managing data traffic within various types of networks. At the core of a network switch's function is the "matching" process. This process is akin to a telephone operator connecting calls; it involves pairing incoming data packets (inputs) with the correct exit paths (outputs). This pairing must happen swiftly and efficiently to ensure data is routed correctly through the network with minimal waiting time. The matching algorithm is pivotal because it determines the switch's overall efficiency, impacting the rate at which data packets are transferred (throughput) and how long they are held before being forwarded (delay).

### The ASPARA Approach
The ASPARA (Adaptive Switching Pattern Algorithm) innovates in the domain of input-buffered switches by integrating two strategic approaches:
1. **Memory Utilization**:
   It proactively stores possible switch configurations for efficient traffic handling.

2. **Parallel Neighbor Exploration**:
   It evaluates multiple switch states in parallel to quickly identify the best one for immediate use.

Together, these strategies enable ASPARA to quickly adapt and optimize network traffic flow, enhancing throughput and minimizing delay.

## Results
The effectiveness of the implemented ASPARA algorithm is evaluated by measuring the average throughput of a network switch for different numbers of ports. below graph is its reslut

![Average Throughput vs. Number of Ports](https://github.com/mahlashrifi/APSARA/blob/master/throughput.png)

