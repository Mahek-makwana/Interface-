# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:36:03 2024

@author: 91990
"""

import time
import random

#Class which represent a Truck with a random number and load
class Truck:
    def __init__(self):
        self.number = random.randint(100, 999)  # Assign a random truck number
        self.load = random.randint(7, 33)  # Assign a random load between 7 and 33 tons

#Class to manage the Warehouse operations
class Warehouse:
    def __init__(self):
        self.dock_gates = [(0, 0), (0, 0), (0, 0)]  # (Truck Number, Load)
        #Parking lot to hold trucks when all the gates are occupied
        self.parking_lot = []
        self.total_trucks = 0
        self.total_load = 0

   #Method to log message to the file
    def log(self, message):
        print(message)  # Print to console
        # Uncomment below to the log to a file
        # with open("logOfDay.txt", "a") as log_file:
        #     log_file.write(message + "\n")

    def arrive_truck(self):
        new_truck = Truck()  # Create a new Truck instance
        self.total_trucks += 1
        self.total_load += new_truck.load
        self.log(f"New Truck: {new_truck.number} with load {new_truck.load} tons")
        self.place_truck(new_truck)
     
    #Method to place the truck in dock gate    
    def place_truck(self, truck):
        for i in range(len(self.dock_gates)):
            if self.dock_gates[i] == (0, 0):  # Check for empty gate 
                self.dock_gates[i] = (truck.number, truck.load)
                self.display_gates()
                return 
        # If all gates are occupied, place in parking lot       
        self.parking_lot.append(truck)
        self.log(f"Truck {truck.number} is in the parking lot!")
    
    #Method to display the state of gates    
    def display_gates(self):
        print("Dock Gates")
        print("________")
        for i, gate in enumerate(self.dock_gates):
            print(f"| G{i + 1} : Truck {gate[0]} - Load {gate[1]}")
            print("|_______")
            print()  # Add space between gates
        print("*************************************")
     
       # Method to check if any trucks are departing from the docks  
    def check_truck_departures(self):
        for i in range(len(self.dock_gates)):
            if self.dock_gates[i] != (0, 0):  # Check if the gate is occupied
                if random.random() < 0.3:  # 30% chance to leave
                    departing_truck = self.dock_gates[i][0]
                    self.log(f"Truck {departing_truck} is leaving the dock!")
                    self.dock_gates[i] = (0, 0)  # Free the gate
                    self.display_gates()
                    self.move_truck_from_parking()  # Move a truck from parking if available
            
    def move_truck_from_parking(self):
        if self.parking_lot:
            truck = self.parking_lot.pop(0)  # First in, first out
            self.place_truck(truck)

    def check_parking_lot(self):
        if len(self.parking_lot) > 0:  # Check if there are trucks in the parking lot
            self.log("Parking Lot Status:")
            for truck in self.parking_lot:
                self.log(f"Truck {truck.number} - Load {truck.load} tons")
        else:
            self.log("No trucks in the parking lot.")

    def summary(self):
        self.log(f"Total Trucks: {self.total_trucks}")
        self.log(f"Load transported during the day: {self.total_load} tons")

#Main phase/program execution
if __name__ == "__main__":
    warehouse = Warehouse()

    for _ in range(10):  # Simulate 10 trucks arriving 
        warehouse.arrive_truck()
        warehouse.check_truck_departures()
        time.sleep(2)  # Wait for 2 seconds

    warehouse.summary()
    warehouse.log("Summary logged to logOfDay.txt")