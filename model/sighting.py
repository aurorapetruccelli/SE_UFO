import datetime
from dataclasses import dataclass

@dataclass
class Sighting:
    id: int
    s_datetime: datetime.datetime
    city:str
    state:str
    country:str
    shape:str
    duration:int
    duration_hm:str
    comments:str
    date_posted:datetime.datetime
    latitude:str
    longitude:str


    def __repr__(self):
        return f"{self.id} {self.s_datetime}"






