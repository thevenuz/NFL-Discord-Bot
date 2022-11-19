from dataclasses import dataclass, field
from typing import Dict, Any
import enum

class GameStatus(enum.Enum):
    Completed= "completed"
    Ongoing = "ongoing"
    YetToStart = "yettostart"

@dataclass 
class Team:
    Name: str = ""
    DisplayName: str = ""
    Color : str = ""

@dataclass
class Score:
    Team: Team = Team()
    Score: int = 0
    Winner: bool = False
    Status : GameStatus = GameStatus.YetToStart

@dataclass 
class Game:
    Game: dict[str, Score] = field(default_factory=dict)

