from dataclasses import dataclass
@dataclass
class State:
    id:str
    name: str
    capital: int
    lat: int
    lng: int
    area: int
    population: int
    neighbors: str

    def __hash__(self):
        return hash(self.id)

