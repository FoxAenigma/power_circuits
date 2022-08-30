#Self-built classes
from nodes import Node

#Built-in modules
from dataclasses import dataclass
from typing import List
from typing import Dict
import numpy as np

def to_complex(polar: tuple):
    r = polar[0]
    phi = polar[1]*np.pi/180
    return r * (np.cos(phi) + np.sin(phi)*1j)

def to_magnitude(polar: tuple):
    return polar[0]

@dataclass
class PowerCircuit:
    node_map: Dict[str, Node]
    admittanceMT: np.ndarray = None
    impedanceMT: np.ndarray = None
    injected_current: np.ndarray = None
    injected_power = None
    transfer_power = None
    system_current = None
    voltage_vector: np.ndarray = None

    def vectorize_voltage(self):
        dim = len(self.node_map.keys())
        vector = np.zeros((dim, dim), dtype=complex)
        for i in range(dim):
            vector[i] = to_complex(self.node_map[i+1]._voltage)
        self.voltage_vector = vector
        return
    
    def compute_admittance(self):
        nmap=self.node_map
        dim = len(self.node_map.keys())
        y_matrix = np.zeros((dim, dim), dtype=complex)
        for i in range(dim):
            for j in range(dim):
                if i==j:
                    for relation in nmap[i+1]._connection.values():
                        y_matrix[i,j] += relation._y
                elif nmap[i+1]._connection.get(j+1) != None:
                    y_matrix[i,j] = -nmap[i+1]._connection[j+1]._y
        self.admittanceMT = y_matrix
        return

    def compute_impedance(self):
        self.impedanceMT = np.linalg.inv(self.admittanceMT)
        return

    def compute_injectedI(self):
        dim = len(self.node_map.keys())
        current = np.zeros((dim, 1), dtype=complex)
        for i in range(dim):
            for k in self.node_map[i+1]._connection.keys():
                current[i] += self.admittanceMT[i,k-1]*to_complex(self.node_map[k]._voltage)
        self.injected_current = current
        return

    def compute_injectedP(self):
        self.vectorize_voltage()
        self.injected_current = np.dot(self.admittanceMT, self.vector_voltage)
        return

    def compute_transferP(self):
        #Transfer power         
        return
    
    def compute_systemI(self):
        #System currents
        return
    
    def compute_losses(self, method: str):
        #Losses
        return


