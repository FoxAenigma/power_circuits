from lines import PILine

from dataclasses import dataclass
from typing import Tuple
from typing import List
from typing import Dict

@dataclass
class Node:
    _index: int
    _voltage: Tuple[float, float] #Polar number
    _connection: Dict[int, PILine]
    
    _active_powerDem: float = None
    _reactive_powerDem: float = None
    _active_powerGen: float = None
    _reactive_powerGen: float = None
    _angle: float = None



