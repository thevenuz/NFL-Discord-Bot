from dataclasses import dataclass


@dataclass
class Config:
    Token: str = ""
    PublicLogChannel: str = ""
    PrivateLogChannel: str = ""
