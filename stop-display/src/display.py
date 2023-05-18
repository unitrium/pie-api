from src.query import Departure
from datetime import datetime
from typing import List, Set, Dict

def filter_departures(departures: List[Departure], lines_directions: Dict[str, Set[str]], vehicle_types: Set[str]) -> List[Departure]:
    return list(filter(
        lambda departure : departure.line in lines_directions.keys() and departure.direction in lines_directions.get(departure.line, set()) and departure.vehicle_type in vehicle_types,
        departures
    ))

def group_by_line(departures: List[Departure]) -> Dict[str, List[Departure]]:
    grouping: Dict[str, List[Departure]] = dict()
    for departure in departures:
        if not departure.line in grouping:
            grouping[departure.line] = list()
        grouping[departure.line].append(departure)
    return grouping

def create_display_ttgo(departures: List[Departure], lines_directions: Dict[str, Set[str]], vehicle_types: Set[str]) -> str:
    stop = departures[0].stop
    now = datetime.now()
    filtered_departures = filter_departures(
        departures,
        lines_directions,
        vehicle_types
    )
    grouped_departures = group_by_line(filtered_departures)
    groups = ""
    for line, departures in grouped_departures.items():
        groups+= f"{line}: "
        for departure in departures:
            time = (departure.departure_datetime - now).total_seconds()
            if time < 0 :
                # If the vehicule is still present in the API call,
                # it means that it is late.
                continue
            minutes = int(time // 60)
            seconds = " 30" if time % 60 > 30 else ""
            groups+= f"{minutes} min{seconds}, "
        groups+= "\n"
    return f"""
    [{stop}] \n
    {groups}
    """
