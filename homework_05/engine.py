"""
dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine():
    volume: float = 2.5
    pistons: int = 4
