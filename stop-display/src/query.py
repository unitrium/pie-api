import requests
from typing import List
from datetime import datetime

BASE_URL = "http://xmlopen.rejseplanen.dk/bin/rest.exe/departureBoard"

class Departure:
    departure_datetime: datetime
    line: str
    direction: str
    vehicle_type: str
    stop: str
    def __init__(self, time: str, date: str, line: str, direction: str, vehicle_type: str, stop: str) -> None:
        self.line = line
        self.direction = direction
        self.vehicle_type = vehicle_type
        self.stop = stop

        self.departure_datetime =  datetime.strptime(f"{date} {time}", "%d.%m.%y %H:%M")
    
    def __str__(self) -> str:
        return f"{self.line}: ({self.direction}) {self.departure_datetime}"

def query_stop_board(stop_id: str, useBus: bool= True, useTrain: bool = True) -> List[Departure]:
    session  = requests.Session()
    params = {
        "id": stop_id,
        "useBus": int(useBus),
        "useTog": int(useTrain),
        "format": "json"
    }
    departure_board = session.get(BASE_URL, params=params).json()["DepartureBoard"]["Departure"]
    return [
        Departure(departure["time"], departure["date"], departure["line"], departure["direction"], departure["type"], departure["stop"])
        for departure in departure_board
    ]
