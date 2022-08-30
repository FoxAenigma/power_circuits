import sys
sys.path.append("/home/FoxyLuxe/Repo/tasks/power_circuits/src/structures")

from src.structures.circuits import PowerCircuit
from src.structures.nodes import Node
from src.structures.lines import PILine

zl = 0.0013+0.003j
bc = 0+0.0008j

node_map = {
    1: Node(
           _index = 1, 
           _voltage = (1.045, 0), 
           _connection = {
                4: PILine(_distance=190, _Zl=zl, _Bc=bc),
                2: PILine(_distance=130, _Zl=zl, _Bc=bc),
                3: PILine(_distance=135, _Zl=zl, _Bc=bc),
           }
       ),
    2: Node(
           _index = 2,
           _voltage = (0.982, -2.8),
           _connection = {
               1: PILine(_distance=130, _Zl=zl, _Bc=bc),
               4: PILine(_distance=100, _Zl=zl, _Bc=bc),
           }
       ),
    3: Node(
           _index = 3,
           _voltage = (0.97, -5.5),
           _connection = {
               1: PILine(_distance=135, _Zl=zl, _Bc=bc),
               5: PILine(_distance=150, _Zl=zl, _Bc=bc),
           }
       ),
    4: Node(
           _index = 4,
           _voltage = (0.96, -4.2),
           _connection = {
               1: PILine(_distance=190, _Zl=zl, _Bc=bc),
               2: PILine(_distance=100, _Zl=zl, _Bc=bc),
               5: PILine(_distance=110, _Zl=zl, _Bc=bc),
           }
       ),
    5: Node(
           _index = 5,
           _voltage = (1.08, -1.2),
           _connection = {
               4: PILine(_distance=110, _Zl=zl, _Bc=bc),
               2: PILine(_distance=120, _Zl=zl, _Bc=bc),
               3: PILine(_distance=150, _Zl=zl, _Bc=bc),
           }
       ),
}

if __name__ == "__main__":
    circuit = PowerCircuit(node_map=node_map)
    #Computation instance methos
    circuit.compute_admittance()
    circuit.compute_impedance()

    #Printable atributtes
    print("Adminttance matrix")
    print(circuit.admittanceMT)
    print()
    print("Impedance matrix")
    print(circuit.impedanceMT)
