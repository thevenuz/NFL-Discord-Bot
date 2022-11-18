from dataclasses import dataclass
from typing import Dict, Any


@dataclass 
class Team:
    Name: str = ""
    DisplayName: str = ""
    Color : str = ""

@dataclass
class Score:
    Team: Team = Team()
    Score: int = 0
    Winner: bool= False

@dataclass 
class Game:
    Game: Dict[str, Score] = {}
