from lines import PILine

from dataclasses import dataclass
from typing import Tuple
from typing import List
from typing import Dict

@dataclass
class Node:
    _index: int
    _connection: Dict[int, PILine]
    
    _active_powerDem: float = None  #No controled variable
    _reactive_powerDem: float = None #No controled variable
    _active_powerGen: float = None #Control variable
    _reactive_powerGen: float = None #Control variable
    _voltage: Tuple[float, float] #State variable (Polar number)
    _angle: float = None #State variable



