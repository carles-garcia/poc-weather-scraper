from dataclasses import dataclass
from typing import Optional


@dataclass
class AverageTemperatures:
    max: Optional[float] = None
    min: Optional[float] = None
