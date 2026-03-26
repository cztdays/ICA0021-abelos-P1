import json
from typing import Dict


def count_people_by_location(filename: str) -> Dict[str, int]:

    with open(filename, 'r', encoding='utf-8') as f:
        people = json.load(f)
    location_count = {}
    for person in people:
        location = person.get('location')
        if location:
            location_count[location] = location_count.get(location, 0) + 1
    return location_count
