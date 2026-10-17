import sys
import json
from pathlib import Path
from typing import Any
import requests
from bs4 import BeautifulSoup
import lxml
import re

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

PATH_EVENT = Path(__file__).parent
PATH_CIRCLES_JSON = PATH_EVENT / "circles.json"
NAME = PATH_EVENT.name

PATH_SCRAPE = PATH_EVENT / "yumemichi2024"
PATH_SCRAPED_JSON = PATH_SCRAPE / "event.json"


def main():
    """Create circles.json"""
    print(f"Retrieving circles information for {NAME} ...")

    # Load events.json
    if not PATH_SCRAPED_JSON.exists():
        raise FileNotFoundError(f"Scraped JSON file not found: {PATH_SCRAPED_JSON}")
    with open(PATH_SCRAPED_JSON, "r", encoding="utf-8") as f:
        events_data = json.load(f)

    event = Event.load_from_json(events_data)
    if not event.circles:
        raise ValueError(f"No circles found in the scraped event data: {PATH_SCRAPED_JSON}")
    for circle in event.circles:
        if circle.media:
            for medium in circle.media:
                medium_path = medium.path
                medium.path = f"02_{medium_path}"  # Update path to include the scrape directory

    # Save the extracted circle information to a JSON file
    with open(PATH_CIRCLES_JSON, "w", encoding="utf-8") as f:
        json.dump([c.get_json() for c in event.circles], f, ensure_ascii=False, indent=2)
    print(f"Saved {len(event.circles)} circles to {PATH_CIRCLES_JSON}")


if __name__ == "__main__":
    main()
